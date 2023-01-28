import math

def findY(x):
    y = 2 - x + ((3/7)*x**2) - ((5/11)*x**3) + math.log10(x)
    return y

x = int(input())
print(findY(x))