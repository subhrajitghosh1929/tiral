# to break up a 6 digit into 3 two digit numbers
num=int(input("Enter 6 digit number: "))
if num<100000 or num>999999:
    print("please enter 6 digit: ")
else:
    n1=num%100          # last 2 digits of the number
    int1=num//100
    n2=int1%100         # middle 2 digits of the number
    int2=int1//100
    n3=int2%100         # first 2 digits of the number
    print("Three 2-digit number are",n3,n2,n1)

    
print()
print("#2")
# to find the first, middle and last digit of a number
import math
num=int(input("Enter a number: "))
if len(str(num))%2 == 0:
    print("please enter odd number of digits : ")
else:
    n1=num%10          # last digit of the number
    n2=str(num)[len(str(num))//2 ]         # middle  digit of the number
    n3=num // pow(10,len(str(num))-1)        # first digit of the number
    print("first digit is :",n3)
    print("middle digit is : " ,n2)
    print("last digit is :",n1)

