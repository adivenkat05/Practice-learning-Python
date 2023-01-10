num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

try:
    print("FILE OPENED")
    print(f"Num1 / Num2 = {num1/num2}")  # If the input is 5, 0.

except ZeroDivisionError:  # executes only if there is Zero Division Error.
    print("You cannot divide a number by zero!!")

except Exception:  # includes all type of error.
    print("Something went wrong.")

finally:
    # Finally block will executed if we get error as well as we don't if we don't get an error.
    print("FILE CLOSED") 

    
