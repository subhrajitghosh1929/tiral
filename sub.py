#WAP with a menu to represent the calculator
print(''' menu 
+ addition
- substraction
* multiplication
/ divition
^ power
''')
num1=eval(input(" Enter the value 1: "))
num2=eval(input(" Enter the value 2: "))
opr=input("Enter the opr (+,-,*,/,^)")
if opr=="+":
        print(num1+num2)
elif opr=="-":
    if num1>num2:
        print(num1-num2,"first")
    elif num2>num1:
        print(num2-num1,"second")
    else:
        print("num1=num2")
elif opr=="*":
    print(num1*num2)
elif opr=="/":
    if num1>num2:
       print(num1/num2,"first")
    elif num2>num1:
        print(num1/num2,"second")
    else:
        print("num1=num2")
elif opr=="^":
    print(num1^num2)    
else:
    print("invalid operator")
    print("use only the operator specified")
print(" end of program ")
 
 
    
   
   
   
