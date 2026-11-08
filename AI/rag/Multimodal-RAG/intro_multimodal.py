import chromadb
import warnings
from pathlib import Path
from chromadb.utils.data_loaders import ImageLoader
from chromadb.utils.embedding_functions import OpenCLIPEmbeddingFunction
from matplotlib import pyplot as plt

curr_path = str(Path(__file__).resolve().parent)
#print(curr_path)

#suppress all warning
warnings.filterwarnings("ignore")

# create a chromadb object
chroma_client = chromadb.PersistentClient(curr_path+"\\data\\crhoma_db")

# instantiate image loader
image_loader = ImageLoader()

# instantiate multimodal embedding function
embedding_function = OpenCLIPEmbeddingFunction()

# create the collection of vector database
collection = chroma_client.get_or_create_collection(
    name="multimodal_collection",
    embedding_function=embedding_function,
    data_loader=image_loader
)

#Add image to collection add() then update() method
collection.update(
    ids=["0","1"],
    uris=[curr_path+"\\images\\lion.jpg" , curr_path+"\\images\\tiger.jpg"],
    metadatas=[{"category":"animal"},{"category":"animal"}]
)

#print(collection.count())

# Use .add() to add a new record or .update() to update existing record
# on first run add() is used, on subsequent runs update() is used
collection.update(
    ids=[
        "E23",
        "E25",
        "E33"
    ],
    uris=[
        curr_path+"\\images\\E23-2.jpg",
        curr_path+"\\images\\E25-2.jpg",
        curr_path+"\\images\\E33-2.jpg"
    ],
    metadatas=[
        {
            "item_id": "E23",
            "category": "food",
            "item_name": "Braised Fried Tofu with Greens",
        },
        {
            "item_id": "E25",
            "category": "food",
            "item_name": "Sauteed Assorted Vegetables",
        },
        {
            "item_id": "E33", 
            "category": "food", 
            "item_name": "Kung Pao Tofu"
        }
    ]
)

#print(collection.count())

# Simple function to print the results of a query.
# The 'results' is a dict {ids, distances, data, ...}
# Each item in the dict is a 2d list.
def print_query_results(query_list: list, query_result: dict) -> None:
    result_count = len(query_result["ids"][0])
    
    for i in range(len(query_list)):
        print(f"Result for query: {query_list[i]}")
        
        for j in range(result_count):
            id = query_result["ids"][i][j]
            distance = query_result["distances"][i][j]
            data = query_result["data"][i][j]
            document = query_result["documents"][i][j]
            metadata = query_result["metadatas"][i][j]
            uri = query_result["uris"][i][j]
            
            print(
                f"id: {id}, distance: {distance}, metadata: {metadata}, document: {document}"
            )
            
            # Display image, the physical file must exist at URI.
            # (ImageLoader loads the image from file)
            print(f"data: {uri}")
            
            #fig, ax = plt.subplot()
            
            plt.imshow(data)
            #plt.axes("off")
            #plt.show()
            plt.draw()
            plt.pause(3)
            plt.cla()
            
            
# It is possible to submit multiple queries at the same time, just add to the list.
query_texts = ["food with carrots", "lion"]

# Query vector db - return 3 results
query_results = collection.query(
    query_texts=query_texts,
    n_results=2,
    include=["documents", "distances", "metadatas", "data", "uris"]
    # where={"category": "animal"}, # filter by metadata - optional - first run remove this
)

print_query_results(query_list=query_texts, query_result=query_results)