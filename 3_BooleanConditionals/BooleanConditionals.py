def can_drive(age):
    """can_drive?
    # As per the rule, you need to be atleast 18 years old to drive car
    Args:
        age (int): age of the person
    """
    return age >=18

print(can_drive(12))
print(can_drive(23))

def is_odd(num):
    return (num % 2) == 1

print(is_odd(100))
print(is_odd(23))

def define(x):
    if x==0:
        print("x is zero")
    elif x > 0:
        print("x is a positive number")
    elif x < 0:
        print("x is a negative number")
    else:
        print("x is not a number, something else")

define(0)
define(23)
define(-12)   