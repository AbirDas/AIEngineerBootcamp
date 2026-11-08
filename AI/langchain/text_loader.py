from langchain_community.document_loaders import TextLoader
from pathlib import Path
import re
from langchain_text_splitters import RecursiveCharacterTextSplitter
#from langchain_openai import OpenAIEmbeddings
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
import pprint

curr_path = str(Path(__file__).resolve().parent)
documents = TextLoader(curr_path+"\\doc\\dream.txt").load()
#print(documnets)
#print()

# Data clean function
def clean_text(text):
    # Remove unwanted characters (e.g., digits, special characters)
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    
    #Normalize whitespace
    text = re.sub(r"\s+", " ", text).strip()
    
    #Convert to lower
    text = text.lower()
    
    return text

# clean the text
#cleaned_document = [clean_text(doc.page_content) for doc in documents]
#print(cleaned_document)

# split text into character
#text_splitter = RecursiveCharacterTextSplitter()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,      # Maximum characters per chunk
    chunk_overlap=100,    # Number of overlapping characters between chunks
    length_function=len  # Strategy to measure length (default is len)
)

#print(text_splitter)
texts = text_splitter.split_documents(documents)
#print("\n",texts)

#Clean up text
texts = [clean_text(text.page_content) for text in texts]
#print(texts)

# Load the OpenAI embeddings to vectorize the text
#embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
embedding = OllamaEmbeddings(model="nomic-embed-text")

# create the retriever from the loaded embeddings and documents
retriever = FAISS.from_texts(texts, embedding).as_retriever(search_kwargs={"k":2})
#print(retriever)

# Query the retriever
# query = "what did Martin Luther King Jr. dream about?"
query = "Give me a summary of the speech in bullet points"
docs = retriever.invoke(query)
#print(docs)

pprint.pprint(f" => DOCS: {docs}:")

# Chat with the model and our docs

from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser

# # Create the chat prompt
prompt = ChatPromptTemplate.from_template(
    "please use the following {docs}, and answer  the following question {query}"
)

# # Create a chat model
model = ChatOllama(model="llama3.2")

chain = prompt | model | StrOutputParser()

response = chain.invoke({"docs": docs, "query": query})
print(f"Model Response::: \n \n {response}")