divby0 = 0
divby5 = 5


def div_met(a,b):
    try:
        print(a/b)
    except ZeroDivisionError as e:
        print(f"Error occured : {e}")
    else:
        print("All is well here")
    finally:
        print("No matter what i will run and execute!")
        
div_met(12,divby0)
print()
div_met(12,divby5)