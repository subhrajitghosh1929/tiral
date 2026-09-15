sum1=sum2=0
num1=int(input("enter number1:"))
num2=int(input("enter number2:"))
num3=int(input("enter number3:"))
sum1=num1+num2+num3
if num1==num2:
    if num3!=num1:
        sum2+=sum3
else:
    if num1==num3:
        sum2+=num2
    else:
        if num1==num3:
         sum2+=num2
        else:
           if num2==num3:
            sum2+=num1
           else:
               sum2+=num1+num2+num3
print("number are",num1,num2,num3)
print("sum of three given number is",sum1)
print("sum of non duplicated number is",sum2)
print()

print("OR")

print()
num1=int(input("enter number1:"))
num2=int(input("enter number2:"))
num3=int(input("enter number3:"))
sum1=num1+num2+num3
sum2=0
if num1!= num2 and num1!= num3:
    sum2+=num1
if num2!= num1 and num2!= num3:
    sum2+=num2
if num3!= num1 and num3!= num2:
    sum2+=num3

print("number are",num1,num2,num3)
print("sum of three given number is",sum1)
print("sum of non duplicated number is",sum2)
print()
