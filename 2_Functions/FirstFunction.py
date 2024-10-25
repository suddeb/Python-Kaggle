def leastDifferences (a, b, c):
    """Return the smallest difference between any two numbers
    among a, b and c.
    
    >>> least_difference(1, 5, -5)
    4
    """
    diff1 = abs(a-b)
    diff2 = abs(b-c)
    diff3 = abs(a-c)
    return min(diff1, diff2, diff3)

print(
    leastDifferences(1, 10, 100),
    leastDifferences(1, 10, 10),
    leastDifferences(5, 6, 7),
)

help(leastDifferences)

print(1,2,3,sep=' < ')

def greeting(who="Deb"):
    print("hello, ",who)
    

greeting()
greeting(who="Sudipta")
greeting("James")