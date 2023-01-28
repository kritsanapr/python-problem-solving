import math

def loop4(a):
    x = 1
    for i in range(4):
        x += (x + (a/x)) / 2
    return x

a = int(input())
print(loop4(a))