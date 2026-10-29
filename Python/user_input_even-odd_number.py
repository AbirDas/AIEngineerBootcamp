
number = int(input("Enter a number, and i will tell if it's even or odd : "))

is_even = ((number%2) == 0)

if is_even:
    print(f"{number} is Even!")
else:
    print(f"{number} is odd!")
