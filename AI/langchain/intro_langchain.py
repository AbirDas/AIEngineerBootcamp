from langchain.chat_models import init_chat_model

from langchain_core.messages import HumanMessage, SystemMessage

from dotenv import load_dotenv
from pathlib import Path

# get path of env file for OpenAI
#path_root = str(Path(__file__).resolve().parent.parent.parent)
#path_env = path_root + "\\.venv\\.env"

#load environmmnet variable
#load_dotenv(path_env)

model = init_chat_model(
    model="llama3.2",
    model_provider="ollama",
)

#response = model.invoke("why is the sky blue?")
#print(response.content)

message = [
    SystemMessage("Translate the following from English into Italian"),
    HumanMessage("Hello")
]

print("message:",message)
print()

response = model.invoke(message)
print(response)
print()
print(response.content)



