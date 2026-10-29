full_name = {"Abir":"Das", "Arun":"Das"}
print(full_name)

print()

person = {"name":"Abir", "age":38, "city":"Bangalore"}
print(person)
print(person["name"])
print(person.get("age"))

print()

person["email"] = "abir@gmail.com"
print(person)
person["is_employed"] = True
print(person)
person["age"] = 35
print(person)

print()

person.pop("age")
print(person)
person.popitem()
print(person)

print()

del person["email"]
print(person)
person.clear()
print(person)
