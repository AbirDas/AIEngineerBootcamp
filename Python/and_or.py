activities = ["hicking", "swiming", "museum", "picnic"]
group_interests = ["art", "history", "swiming"]

# Check if an activity aligns with group intrest
if "museum" in activities and ("art" in group_interests or 
                               "history" in group_interests):
    print("We should visit the museum!")
elif "swiming" in activities and "swiming" in group_interests:
    print("Looks like a day in pool is in order!")
else:
    print("lets plan a picnic")
    
print()

age = 22
if age!=23:
    print("not 23")
    
print()

toppings = ['olives', "tomatoes"]
if toppings[0] != "mangoes":
    print("no mangoes for topping")
    
print()

#day = "Saturday"
day = "Sunday"
fridge_contents = ["eggs","bacon"]
if day == "Saturday":
    if "eggs" and "bacon" in fridge_contents:
        print("Time for a hearty breakfast!")
    else:
        print("Maybe just cereal today!")
else:
    print("Stick to the quick breakfast")
