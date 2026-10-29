
fruits = ["apple", "banana", "cherry"]
print(fruits)
print("index 0 =",fruits[0])
print("index 2 =",fruits[2])

print()

fruits[0] = "mango"
print(fruits)

print()

fruits.append("guava")
print(fruits)
fruits += ["pear", "grape"]
print(fruits)

print()

fruits.remove("cherry")
print(fruits)
#remove the last item
fruits.pop()
print(fruits)
# remove index 0
fruits.pop(0)
print(fruits)

print()

message = f"Hello, my name in abir and i like a good {fruits[1]}"
print(message)

print()

age = [76, 12, 45, 56]
print(f"Before sorting : {age}")
age.sort()
print(f"After sorting : {age}")

print()

fruits.extend(["orange", "mango", "apple"])
print(f"Before sorting : {fruits}")
fruits.sort()
print(f"After sorting : {fruits}")

print()

list_len = len(age)
print(list_len)