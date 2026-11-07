from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate

system_template = "Translate the following from English into {language}"

prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template),("user","{text}")]
)

prompt = prompt_template.invoke({"language":"Bengali","text":"How are you"})

print(prompt)
print()

model = init_chat_model(
    model="llama3.2",
    model_provider="ollama"
)

response = model.invoke(prompt)

print(response)
print()
print(response.content)