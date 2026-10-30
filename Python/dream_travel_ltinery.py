import os
import json

dream_destinations = {}

print("let's plan your dream travel itinerary ->- ")
print("Enter 'done' when you're finished. \n")

while True:
    country = input("Which counrty you would like to visit : ")
    if country.lower().strip() == "done":
        break
    
    note = input(f"Anything specific  you'd like to do or see in {country}? (Press enter to skip) : ")
    
    #add the county and optional note to the dic
    dream_destinations[country] = note if note else "No specific plans"
    
    print("Got it! Let's keep going or type 'done' to finish!")
    
print("\n Your dream travel itinerary:")
for country, activity in dream_destinations.items():
    print(f"-{country}: {activity}")
    
print("\n Looks like a exicting adventure, safe travel")

#Save into file
with open("travel_destination.json", "w") as file:
    json.dump(dream_destinations, file, indent=4)
   
file_path = os.path.abspath("travel_destination.json") 
print("Saved file in travel_destination.json in location:", file_path)

#reading file
with open("travel_destination.json", "r") as file:
    file_content = json.load(file)
    print("Reading file :",file_content)
    
if os.path.exists(file_path):
    os.remove(file_path)
    print(f"Succesfully deleted {file_path}.")
else:
    print(f"The file {file_path} do not exit.")