from random import choice

items = ["apple", "mango", "banana", "guava", "pears"]

def rand_fruit(fruits):
    if not fruits:
        return "The fruit list is empty"
    else:
        return choice(fruits)
    
print("Choice of fruit:",rand_fruit(items))