
#def greet(name):
#    print(f"Hello there {name}")
    
def greet(name,age):
    print(f"Hello {name}, you are {age} old")
    
for i in range(2, 11, 2):
    #greet(f"Abir-{i}")
    greet("Das",i)

print()

def car_info(car_type,car_name):
    print(f"Your {car_type} name is {car_name}")
    
car_info(car_type="truck", car_name="ford")
car_info(car_name="xuv700", car_type="suv")

print()

def function_with_default_value(something="nothing"):
    print(f"You have pass value {something}")
    
function_with_default_value()