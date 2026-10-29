
counter = 0

while counter <= 5:
    print(f"Counter is {counter}")
    counter += 1
    
prompt = "\nEnter 'quit' to end the program."
prompt += "\nEnter your command: "
#print(prompt)

while True:
    input_value = input(prompt)
    print(f"you have enter : {input_value}")
    if input_value.strip() == "quit":
        print("Exiting the program")
        break
    else:
        print("wrong input: program will keep running untill you enter 'quit'")