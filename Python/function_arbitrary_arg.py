
def sum_number(*args):
    return sum(args)
print("The Sum:",sum_number(2, 45, 1, 34, 89, 10))

print()

def build_profile(first, last, **user_info):
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info
print(build_profile("Abir", "Das", age=38, location="India", job="Developer", identity="Ram bhakt" ))