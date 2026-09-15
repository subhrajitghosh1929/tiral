#0
print("#0")
def sum1():     #non-parameterized,func defination, func header 
    print("the sum of two numbers",10+20)   #func body
    return      #return statement
sum1()          #func call

#1
print("#1")
def sum1():     #non-parameterized,func defination, func header
    s=10+20     #func body
    return s    #return statement
print("the sum of two numbers",_name_)   #func call

#2
print()
print("#2")
def sum1():     #non-parameterized,func defination, func header
    num1=20     #func body
    num2=10     #func body
    s=num1+num2     #func body
    return s     #return statement    
print("the sum of two numbers",sum1())      #func call

#3
print()
print("#3")
def sum1():     #non-parameterized,func defination, func header
    num1=int(input("enter a number :"))   #func body  
    num2=int(input("enter a number :"))   #func body
    s=num1+num2                           #func body
    return s     #return statement
print("the sum of two numbers",sum1())          #func call

#4
print()
print("#4")
def sum1():     #non-parameterized,func defination, func header
    num1=eval(input("enter a number :"))    #func body
    num2=eval(input("enter a number :"))    #func body
    return num1+num2     #return statement
print("the sum of two numbers",sum1())       #func call 

#5
print()
print("#5")
def sum1():     #non-parameterized,func defination, func header
    num1=float(input("enter a number :"))   #func body
    num2=float(input("enter a number :"))   #func body                             #func body
    return num1+num2     #return statement
print("the sum of two numbers",sum1())      #func call

#6
print()
print("#6")
def sum1():     #non-parameterized,func defination, func header
    s=num1+num2                         #func body
    return s     #return statement
num1=float(input("enter a number :"))   #func body
num2=float(input("enter a number :"))   #func body
print("the sum of ",num1," and ",num2," is ",sum1())     #func call
