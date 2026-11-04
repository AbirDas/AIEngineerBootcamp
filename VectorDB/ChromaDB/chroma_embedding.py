import chromadb
from chromadb.utils import embedding_functions as embf

#========= Example ======================

default_ef = embf.DefaultEmbeddingFunction()

#name = "Abir Das"
#emb = default_ef(name)
#print(emb)

# ================== example ================

chroma_client = chromadb.Client()

collection_name = "embed_collection"

collection = chroma_client.get_or_create_collection(
    name=collection_name,
    embedding_function=default_ef
)


# Define text documents
documents = [
    {"id": "doc1", "text": "Hello, world!"},
    {"id": "doc2", "text": "How are you today?"},
    {"id": "doc3", "text": "Goodbye, see you later!"},
]

for doc in documents:
    collection.upsert(ids=doc["id"], documents=doc["text"])
    
#define query
query_text = "when will i see you next?"

result = collection.query(
    query_texts=query_text,
    n_results=2
)

print(result)
print()

for idx in enumerate(result["ids"][0]):
    #print(idx)
    doc_id = result["ids"][0][idx[0]]
    distance = result["distances"][0][idx[0]]
    document = result["documents"][0][idx[0]]
    print(
            f" For the query: {query_text}, \n Found similar document: {document} (ID: {doc_id}, Distance: {distance})\n"
        )
    #print(doc_id)
