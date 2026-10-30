
def format_name(first_name,last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

formated_name = format_name("abir", "das")
print(formated_name)

print()

def multiply(a, b):
    """Takes two number and multiplies them.

    Args:
        a (int): integers is passed
        b (int): another integer

    Returns:
        int: the product result
    """
    return a * b

res = multiply(2,3)
print(res)