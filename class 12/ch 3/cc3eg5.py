def myFunc1(a):
    print("\t Inside myFunc1()")
    print("\t Value received in 'a'as ",a)
    a=a+2
    print("\t Value of 'a' now change to",a)
    print("\t returning from my/Func1()")
num=3
print("calling myFunc1()by passing 'num'with value",num)
myFunc1(num)
print("Back from myFunc1().value of'num' is",num)
