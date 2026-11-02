import ollama

#response = ollama.list()
#print(f"available model :-\n{response}")

# == Chat example ==
res = ollama.chat(
    model="llama3.2",
    messages=[
        {"role":"user",
         "content":"Why is the sky blue?"}   
    ],
    stream=True
)

#print(res["message"]["content"])
for chunk in res:
    print(chunk["message"]["content"], end="", flush=True)