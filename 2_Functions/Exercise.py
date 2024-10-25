#Question 1
def round_to_two_places(num):
    """Return the given number rounded to two decimal places. 
    
    >>> round_to_two_places(3.14159)
    3.14
    """
    return round(num,2)
    # Replace this body with your own code.
    # ("pass" is a keyword that does literally nothing. We used it as a placeholder
    # because after we begin a code block, Python requires at least one line of code)
    pass

# Check your answer
# q1.check()

#Question 2
# Put your test code here
print(round(12356892.234,-3))

#Question 3
def to_smash(total_candies,numOfFriends=3):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1
    """
    return total_candies % numOfFriends

# Check your answer
# q3.check()

#Question 4
round_to_two_places(9.9999)
x = -10
y = 5
# Which of the two variables above has the smallest absolute value?
def f(x):
    y = abs(x)
    return y

print(f(5))smallest_abs = min(abs(x), abs(y))
 
 