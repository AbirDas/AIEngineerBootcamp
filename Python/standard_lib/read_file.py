
from pathlib import Path

p = Path(".")
print(p.cwd())
print(p.absolute())

print()

#with open("example.txt", "r") as file:
#    print(file)

path = Path("./standard_lib/example.txt")
content = path.read_text()
print("Original content:-\n",content)

print()
print("Lower content:-\n",content.lower())