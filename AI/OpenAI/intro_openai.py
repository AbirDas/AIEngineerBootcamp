from openai import OpenAI
import os
from pathlib import Path
from dotenv import load_dotenv

dotenv_path = Path("C:\\AKD\\workplace\\AIEngineerBootcamp\\.venv\\.env")

load_dotenv(dotenv_path=dotenv_path)
openai_api_key = os.getenv("OPENAI_API_KEY")
print("openai_api_key:",openai_api_key)
client = OpenAI(api_key= openai_api_key)

model = "gpt-5-nano"

response = client.chat.completions.create(
    model=model,
    messages=[
        {"role":"system", "content":"you are helpfull assistant"},
        {"role":"user","content":"what is the meaning of life"}
    ]
)

print(response.choices[0].message.content)
