class MyCustomError(Exception):
    pass

class ValueTooSmallError(MyCustomError):
    pass

class VlaueTooLargeError(MyCustomError):
    pass

def check_value(number):
    if number < 5:
        raise ValueTooSmallError(f"The value is too small {number}")
    elif number > 50:
        raise VlaueTooLargeError(f"The value is too large {number}")
    else:
        print(f"The {number} is under alowed range")
        
try:
    check_value(2)
except Exception as e:
    print(f"Error with msg :{e}")
finally:
    print()
    
try:
    check_value(60)
except MyCustomError as e:
    print("Error handle :",e)
finally:
    print()

try:
    check_value(10)
except ValueTooSmallError as s:
    print("Error handle : ",s)
except VlaueTooLargeError as l:
    print("Error handle : ", l)  
print()  
