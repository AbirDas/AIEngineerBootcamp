from langchain_community.document_loaders import (
    TextLoader,
    PyPDFLoader,
    CSVLoader,
    DirectoryLoader
)
from pathlib import Path

path = str(Path(__file__).resolve().parent)
dir_loader = DirectoryLoader(path+"\\data\\", glob="**/*.txt")
dir_documents = dir_loader.load()

print("Directory text documents:",dir_documents)

#from langchain_community.document_loaders import 
#libmagic is unavailable but assists in filetype detection. Please consider installing libmagic for better results.