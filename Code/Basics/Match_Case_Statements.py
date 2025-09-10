# Match Case Statements (switch): An alternative to using many 'elif' statements
#                                 Execute some code if a value matches a 'case' 
#                                 Benefits: cleaner and syntax is more readable 

# Example 1:

def day_of_week(day): # Long chain of if -> elif -> else statements
    if day == 1:
        return "It is Sunday"
    elif day == 2:
        return "It is Monday"
    elif day == 3:
        return "It is Tuesday"
    elif day == 4:
        return "It is Wedensday"
    elif day == 5:
        return "It is Thursday"
    elif day == 6:
        return "It is Friday"
    elif day == 7:
        return "It is Saturday"
    else:
        return "Not a valid day"

print(day_of_week(1))


def day_of_week(day): # More readable with case statements
    match day:
        case 1:
            return "It is Sunday"
        case 2:
            return "It is Monday"
        case 3:
            return "It is Tuesday"
        case 4:
            return "It is Wedensday"
        case 5:
            return "It is Thursday"
        case 6:
            return "It is Friday"
        case 7:
            return "It is Saturday"
        case _: # _ is a wildcard (allows final calse to act as an 'else' statement)
            return "Not a valid day"

print(day_of_week(1))


# Example 2:

def is_weekend(day):
    match day:
        case "Saturday" | "Sunday":
            return True
        case "Monday" | "Tuesday" | "Wedensday" | "Thursday" | "Friday": # Can use or to make everything neater
            return False
        case _:
            return False

print(is_weekend("Monday"))