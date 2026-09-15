a=b=c=0
for i in range(1,5):
    a=int(input("enter the number1 :"))
    b=int(input("enter the number2 :"))
    if b==0:
        print("divisor by zero error! abortion! ")
        break
    else:
        c=a//b
        print("Question=",c)
print("program over! ")
