
# Errors can happen in programs, and we need a clean way to handle them
# TODO: This code will cause an error because you can't divide by zero:
# x = x /10
# TODO: Exceptions provide a way of catching errors and then handling them in 
# a separate section of the code to group them together

try: 
    x = 10/0
except:
    print("Caught an error")

# TODO: You can also catch specific exceptions

try: 
    answer = input("Enter a number: ")
    num = int(answer)
except ZeroDivisionError as e:
    print("Dividing by zero is not allowed:")
except ValueError as e:
    print("Invalid input:", e)
finally:
    print("This will always run")