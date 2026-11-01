import json
import os
from pathlib import Path

file_name = "example.json"

dic = {
    "name": "Abir Das",
    "age": 38,
    "job": "Software Developer",
    "bhakt": "Ram & Hanuman bhakt"
}

with open(file_name, "w") as file:
    json.dump(dic, file, indent=4)
    
if os.path.exists(file_name):
    print(f"\n{file_name} is available so reading it.\nValue:-")
    with open(file_name,"r") as file:
        content = json.load(file)
        print(content)
else:
    print(f"File:{file_name} do not present")
    
file_path = os.path.abspath(file_name)
if os.path.exists(file_path):
    input("Once user press enter will delete the file: ")
    print("Now deleting the file, post reading")
    os.remove(file_path)
    
print()

name = ["Abir", "Kumar", "Das"]

with open(file_name, "w") as file:
    content = json.dumps(name)
    file.write(content)
    
if os.path.exists(file_name):
    with open(file_name, "r") as file:
        content = json.load(file)
        print(f"File content:-\n {content}")

if os.path.exists(file_path):
    input("Once user press enter will delete the file: ")
    print("\nNow deleting the file")
    os.remove(file_path)