"""#1
print("#1")
print()
def interest(principal,rate,time):     #(dummy) parameterized func defination, func header
    si=rate*principal*time/100                           #func body
    print("principal",principal)
    print("rate",rate)
    print("time",time)
    return si     #return statement
n1=float(input("enter principal :"))
n2=float(input("enter rate :"))
n3=float(input("enter time :"))
si=interest(n1,n2,n3)
print("the simple interest is :",si)      #(actual)parameterizedfunc call

#2
print("#2")
print()
def interest(prin,ra,ti):     #(dummy) parameterized func defination, func header
    si=ra*prin*ti/100                           #func body
    print("principal",prin)
    print("rate",ra)
    print("time",ti)
    return si     #return statement
prin=float(input("enter principal :"))
ra=float(input("enter rate :"))
ti=float(input("enter time :"))
si=interest(prin,ra,ti)
print("the simple interest is :",si)      #(actual)parameterizedfunc call
"""
#3
print("#3")
print()
def interest(prin,ra,ti):     #(dummy) parameterized func defination, func header
    si=ra*prin*ti/100                           #func body
    print("principal",prin)
    print("rate",ra)
    print("time",ti)
    return si     #return statement
prin=float(input("enter principal :"))
ra=float(input("enter rate :"))
ti=float(input("enter time :"))
si=interest(ra=10,prin=1000,ti=5)
print("the simple interest is :",si)      #(actual)parameterizedfunc call
