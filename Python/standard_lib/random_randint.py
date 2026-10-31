from random import randint

print(randint(a=2, b=9))
print()

items = ['apple', 'banana', 'mangoes', 'guava']

def rend_fruit(fruits):
    rand = randint(a=0, b=len(fruits)-1)
    print("Randomly chose:",fruits[rand])
    
rend_fruit(items)