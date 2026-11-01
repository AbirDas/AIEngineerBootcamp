
fruits = ["apple", "mango", "banana"]

try:
    print(fruits[9])
except IndexError as e:
    print(f"Error thrown with msg : {e}")