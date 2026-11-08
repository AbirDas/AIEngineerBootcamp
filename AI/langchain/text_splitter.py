from langchain_community.document_loaders import TextLoader
from pathlib import Path
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Load your document (assuming a text file for this example)
path = str(Path(__file__).resolve().parent)
text_loader = TextLoader(path+"\\doc\\dream.txt")
documents = text_loader.load()
#print(documents)

# Create text splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20,
    length_function=len
)
#print(text_splitter)

# Split documents
splits = text_splitter.split_documents(documents)

for i, split in enumerate(splits):
    print(f"Split {i+1} : \n{split}\n")
