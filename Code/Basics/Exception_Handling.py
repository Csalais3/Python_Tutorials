# Exception: An event that interrupts the flow of a program
#            (ZeroDivisionError, TypeError, ValueError)
#             1) try (try some code), 2) except (Handle and Exception), 3) finally (Do some cleanup)

try:
    number = int(input("Enter a number: "))
    print(1 / number)
    
except ZeroDivisionError:
    print("You can't divide by 0!")
except ValueError:
    print("You must only enter nunmbers!")
except Exception:
    print("Something went wrong!")
finally: # Always Excecutes regardless of the occurrence of an exception
    print("Do some cleanup here")
