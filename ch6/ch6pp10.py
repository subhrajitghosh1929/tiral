h = float(input("Enter height of the triangle: "))
b = float(input("Enter base of the triangle: "))
area = 0.5 * b * h
print("Area of triangle = ", area)

print()
print("#2")
import math
a=float(input("Enter length of side a: "))
b = float(input("Enter length of side b: "))
c = float(input("Enter length of side c: "))
s = (a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Area of triangle = ", area,"sq.units")
