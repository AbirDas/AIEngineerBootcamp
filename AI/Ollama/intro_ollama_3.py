import ollama


# ==================================================================================
# ==== The Ollama Python library's API is designed around the Ollama REST API ====
# ==================================================================================

# == Generate example ==
# res = ollama.generate(
#    model="llama3.2",
#    prompt="why is sea water salty?",
#    max_tokens=50
#)

# Show
# print(ollama.show("llama3.2"))

ollama.create(
    model="OceanExpert",
    from_="llama3.2",
    system="you are very smart assistant who knows everything about oceans, you are very succint and informative.",
    parameters={
        "temperature" : 0.1,
        "topk" : 0.8        
    }
)

res = ollama.generate(
    model="OceanExpert",
    prompt="Why is the ocean so salty?",
    stream=True
)

for chunk in res:
    print(chunk["response"], end="", flush=True)
#print(res["response"])

# List model
print("\nOllama model list:-",ollama.list())

# Delete created model
ollama.delete("OceanExpert")

# List model
print("\nAfter deleting, Ollama model list:-",ollama.list())
