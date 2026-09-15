tup = eval(input("Enter the elements of tuple:"))
b = int(eval(input("Enter the index value:")))
c = len(tup)
if b < c:
    print("value of tuple at index", b ,"is:" ,tup[b])
else:
    print("Index is out of range")


#2b
term = int(input ("Enter Fibonacci Term: "))
lst = [0,1]
a = 0
b = 1
c = 0
for i in range(term+1):
    c = a + b
    a = b
    b = c
    lst.append(c)
tup=tuple(lst)
print("Terms of Fibonacci series are:",tup)
ele=eval(input("Enter the index value:"))
print("index of ",ele,"is ",tup.index(ele))
