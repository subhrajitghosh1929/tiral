# to find the largest among 3 numbers
num1=float(input("Enter 1st number: "))
num2=float(input("Enter 1st number: "))
num3=float(input("Enter 1st number: "))


if (num1 > num2) and(num1 > num3):
    largest=num1
elif (num2 > num1) and(num2 > num3):
    largest=num2
else:
    largest=num3


if (num1 < num2) and(num1 < num3):
    smallest=num1
elif (num2 < num1) and(num2 < num3):
    smallest=num2
else:
    smallest=num3


if (num1 < largest) and(num1 > smallest):
    mid=num1
elif (num2 <largest) and(num2 > smallest):
    mid=num2
else:
    mid=num3

    
print("smallest among 3 numbers is : ",smallest)
print("middle among 3 numbers is : ",mid)
print("largest number is: ",largest)
