'''
    C**2 = a**2 + b**2 - 2abcos(C)
'''

import math

def triangle():
    a = float(input("Enter the value of a: "))
    b = float(input("Enter the value of b: "))
    C = float(input("Enter the value of C: "))
    c = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(C))
    return c


print('c =' ,triangle(), 'cm.')