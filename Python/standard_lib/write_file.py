from pathlib import Path

content = "Abir is writing code!"
content += "\nand i like to write python code"
content += "\nits a lovely thing."

path = Path('test.txt')
path.write_text(content)

