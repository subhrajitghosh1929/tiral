# type c data handaling
#pg-220

#1
p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))
si = p * r * t / 100
print("Simple Interest =", si)

#2
d1 = float(input("Enter Sunday Temperature: "))
d2 = float(input("Enter Monday Temperature: "))
d3 = float(input("Enter Tuesday Temperature: "))
d4 = float(input("Enter Wednesday Temperature: "))
d5 = float(input("Enter Thursday Temperature: "))
d6 = float(input("Enter Friday Temperature: "))
d7 = float(input("Enter Saturday Temperature: "))
avg = (d1 + d2 + d3 + d4 + d5 + d6 + d7) / 7
print("Average Temperature =", avg)

#3
import math

x = int(input("Enter x: "))
y = int(input("Enter y: "))
z = int(input("Enter z: "))
res = 4 * x ** 4 + 3 * y ** 3 + 9 * z + 6 * math.pi
print("Result =", res)

#4
totalSecs = int(input("Enter seconds: "))
mins = totalSecs // 60
secs = totalSecs % 60
print(mins, "minutes and", secs, "seconds")

#5
y = int(input("Enter year to check: "))
print(y % 4 and "Not a Leap Year" or "Leap Year")

#6
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print(x % y and "Not Fully Divisible" or "Fully Divisible")

#7
x = int(input("Enter a two digit number: "))
y = x % 10 * 10 + x // 10
print("Reversed Number:", y)

#8
x = int(input("Enter a three digit number: "))
d1 = x % 10
x //= 10
d2 = x % 10
x //= 10
d3 = x % 10
y = d1 * 100 + d2 * 10 + d3
print("Reversed Number:", y)

#9
d = int(input("Enter day: "))
m = int(input("Enter month: "))
n = (m - 1) * 30 + d
print("Day of the year:", n)

#10
y = float(input("How many years? "))

d = y * 365
h = d * 24
m = h * 60
s = m * 60

print(y, "years is:")
print(d, "days")
print(h, "hours")
print(m, "minutes")
print(s, "seconds")

#11
a = int(input("What is your age? "))
print("In ten years, you will be", a + 10, "years old!")

#12
import random

a = random.randint(0, 5)
b = random.randint(0, 5)
c = a ** b
print("Random number between 0 and 5 (A) :", a)
print("Random number between 0 and 5 (B) :", b)
print("A to the power B =", c)
#14
a=random.randrange
b=random.randrange
c=random.randrange
print("general number:",a,b,c)
#15
import random
otp = random.randint(100000, 999999);
print("OTP:", otp);
#17
import math
a = float(input("Enter base: "))
b = float(input("Enter height: "))
x = float(input("Enter angle: "))
c = math.sqrt(a ** 2 + b ** 2)
print("Hypotenuse =", c)
#18
import math
area = float(input("Enter area of sphere: "))
r = math.sqrt(area / (4 * math.pi))
print("Radius of sphere =", r)
#19
str = input("Enter string: ")
len = len(str)
opStr = str * len
print("Result", opStr)
#20
import math
r = 8
h = 15
v = math.pi * r * r * h
print("Volume of Cylinder =", v)
#21
import math
side = float(input("Enter side: "))
area = math.sqrt(3) / 4 * side * side
print("Area of triangle =", area)
#22
import math
side = float(input("Enter side: "))
area = math.sqrt(3) / 4 * side * side
print("Area of triangle =", area)
#23
p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))
si = p * r * t / 100
amt = p + si
print("Amount Payable =", amt)
#24
p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))
amt = p * (1 + r / 100) ** t

print("Amount Payable =", amt)
#25
a = int(input("Enter a: "))
b = int(input("Enter b: "))
res = a ** 3 + b ** 3 + 3 * a ** 2 * b + 3 * a * b ** 2
print("Result =", res)

#26
print(type(6+3))

