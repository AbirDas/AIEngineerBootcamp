person = {"name":"Abir", "age":38, "city":"Bangalore"}

person["email"] = "abir@gmail.com"
person["is_employed"] = True
person["age"] = 35

#Get Keys
for key in person:
    #print(f"Keys: {key}, Value: {person.get(key)}")
    print(f"Keys: {key}, Value: {person[key]}")

print()

#Get values
for value in person.values():
    print("Getting values only:",value)
    
print()

#Get Keys and Values
for key, value in person.items():
    print(key,value)