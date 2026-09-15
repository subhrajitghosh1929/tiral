#0
print("#0")
def sum1():     #non-parameterized func defination, func header 
    print("the sum of two numbers",10+20)   #func body
    return      #return statement
sum1()          #func call

#1
print("#1")
def sum1():     #non-parameterized func defination, func header
    s=10+20     #func body
    return s    #return statement
print("the sum of two numbers",sum1())   #func call

#2
print()
print("#2")
def sum1(n1,n2):     #(dummy) parameterized func defination, func header
    s=n1+n2     #func body
    return s     #return statement    
print("the sum of two numbers",sum1(10,20))      #(actual)parameterized func call

#3
print()
print("#3")
def sum1(n1,n2):     #(dummy) parameterized func defination, func header
    s=n1+n2                           #func body
    return s     #return statement
num1=68 
print("the sum of two numbers",sum1(num1,12))          #(actual)parameterized func call

#4
print()
print("#4")
def sum1(n1,n2):     #(dummy) parameterized func defination, func header
    s=n1+n2                             #func body
    return s    #return statement
num1=eval(input("enter a number :"))    
num2=24    
print("the sum of two numbers",sum1(num1,num2))       #(actual)parameterized func call 

#5
print()
print("#5")
def sum1(n1,n2):     #(dummy) parameterized func defination, func header
    s=n1+n2                             #func body
    return s     #return statement
num1=10   
num2=float(input("enter another number :"))   
print("the sum of two numbers",sum1(num1,num2))      #(actual)parameterizedfunc call

# logical error 
"""#6
print()
print("#6")
def sum1(n1,n2):     #(dummy) parameterized func defination, func header
    s=n1+n2                         #func body
    return s     #return statement
# logical error 
print("the sum of ",num1," and ",num2," is ",sum1(10,20))  #(actual)parameterized func call
"""
#6
print()
print("#6")
def sum1(n1=10,n2=20):     #(actual) parameterized func defination, func header
    s=n1+n2                         #func body
    return s     #return statement   
print("the sum of two numbers is ",sum1())  #non-parameterized func call

#7
print()
print("#7")
def sum1(n1,n2):     #(dummy) parameterized func defination, func header
    s=n1+n2                             #func body
    return s     #return statement
num1=10   
num2=float(input("enter another number :"))   
print("the sum of two numbers",sum1(num1+2,num2))      #(actual)parameterizedfunc call

#8
print()
print("#8")
def sum1(n1,n2=10):     #(dummy) parameterized func defination, func header
    s=n1+n2                             #func body
    return s     #return statement
n1=float(input("enter another number :"))
s=sum1(n1)
print("the sum of two numbers",s)      #(actual)parameterizedfunc call

#9
print()
print("#9")
def sum1(n1,n2=10):     #(dummy) parameterized func defination, func header
    s=n1+n2                             #func body
    return s     #return statement
n1=float(input("enter another number :"))
n2=float(input("enter another number :"))
s=sum1(n1,n2)
print("the sum of two numbers",s)      #(actual)parameterizedfunc call

