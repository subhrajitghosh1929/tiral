print('''
+ addition
- substraction
* multiplication
/ divition
^ power
''')
num1=eval(input(" Enter the value 1:-"))
num2=eval(input(" Enter the value 2:-"))
opr=input("Enter the opr (+,-,*,/,^)")
if opr=="+":
    print(num1+num2)
elif opr=="-":
    print(num1-num2)
elif opr=="*":
    print(num1*num2)
elif opr=="/":
    print(num1/num2)
elif opr=="^":
    print(num1^num2)    
else:
    print("invalid operator")
    print("use only the operator specified")
print(" end of program ")
