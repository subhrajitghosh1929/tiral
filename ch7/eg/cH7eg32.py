import math
a=int(input("Enter he length of side a :"))
b=int(input("Enter he length of side b :"))
c=int(input("Enter he length of side c :"))
s=(a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))      
print("area of a triangle",area)
