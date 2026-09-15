lst = [0,1]
a = 0
b = 1
c = 0
for i in range(7):
    c = a + b
    a = b
    b = c
    lst.append(c)
tup=tuple(lst)
print("Terms of Fibonacci series are:",tup)
ele=eval(input("Enter the index value:"))
print("index of ",ele,"is ",tup.index(ele))
