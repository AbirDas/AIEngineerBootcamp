import chromadb
#import sys
from chromadb.utils import embedding_functions as ef
from pathlib import Path

current_folder = str(Path(__file__).resolve().parent)
current_folder += "\\db\\chroma_persist"
#print(current_folder)
#sys.exit()

default_ef = ef.DefaultEmbeddingFunction()
chroma_client = chromadb.PersistentClient(path=current_folder)

collection = chroma_client.get_or_create_collection(
    name="persist_first_test",
    embedding_function=default_ef
)

# Define text documents
documents = [
    {"id": "doc1", "text": "Hello, world!"},
    {"id": "doc2", "text": "How are you today?"},
    {"id": "doc3", "text": "Goodbye, see you later!"},
    {"id": "doc4", "text": "Microsoft is a technology company that develops software. It was founded by Bill Gates and Paul Allen in 1975."}
]

for doc in documents:
    collection.upsert(ids=doc["id"], documents=doc["text"])
    
# define a query text
query_text = "find document related to technology company"

results = collection.query(
    query_texts=query_text,
    n_results=2
)

for idx, doc_id in enumerate(results["ids"][0]):
    distance = results["distances"][0][idx]
    document = results["documents"][0][idx]
    
    print(
        f"\n For the query: {query_text}, \n Found similar document: {document} (ID: {doc_id}, Distance: {distance})\n"
    )