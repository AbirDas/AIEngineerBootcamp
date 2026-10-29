family = {
    "mon" : {"name":"Kausalya", "age":60},
    "dad" : {"name":"Dasharatha", "age":75}
}

for name, information in family.items():
    #print(name,information)
    print(f"parent type:{name}")
    parent_name = information["name"]
    parent_age = information["age"]
    print(f"name: {parent_name}, age: {parent_age}\n")