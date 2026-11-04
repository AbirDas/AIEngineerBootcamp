import os
from dotenv import load_dotenv
from openai import OpenAI
from pathlib import Path

path = str(Path(__file__).resolve().parent.parent.parent)
path += "\\.venv\\.env"
#print(path)

load_dotenv(path)

openai_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=openai_key)

response = client.embeddings.create(
    input ="Your text string goes here",
    model="text-embedding-3-small"
)

print(response)
print(len(response.data[0].embedding))