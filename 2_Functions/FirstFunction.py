def leastDifferences (a, b, c):
    diff1 = abs(a-b)
    diff2 = abs(b-c)
    diff3 = abs(a-c)
    return min(diff1, diff2, diff3)

print(
    leastDifferences(1, 10, 100),
    leastDifferences(1, 10, 10),
    leastDifferences(5, 6, 7),
)