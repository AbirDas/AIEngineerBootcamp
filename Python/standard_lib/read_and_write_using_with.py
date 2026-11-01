from pathlib import Path

content = "Abir is writing code!"
content += "\nand i like to write python code"
content += "\nits a lovely thing."

with Path.open("example.txt", "r") as file:
    contxt = file.read()
    print(contxt)
    
with Path.open("example.txt", "w") as file:
    print(file.write(content))