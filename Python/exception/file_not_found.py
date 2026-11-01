
from pathlib import Path

path = Path("example.txt")

try:
    print(path.read_text())
except FileNotFoundError as e:
    print(f"Error with msg : {e}")

