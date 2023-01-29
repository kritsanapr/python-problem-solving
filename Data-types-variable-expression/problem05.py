# Triangle
'''
    area = 1/2 * ab * sin(C)
'''
import math

a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
C = float(input("Enter the value of C: "))

def area(a,b,C):
    CR = C * math.pi/180
    area = (1/2) * a * b * math.sin(CR)
    return area

print("area = " , area(a,b,C), "sq cm")