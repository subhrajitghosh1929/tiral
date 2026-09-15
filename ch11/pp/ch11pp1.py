lst = [0,1]
a = 0
b = 1
c = 0
for i in range(7):
    c = a + b
    a = b
    b = c
    lst.append(c)
print("9 terms of Fibonacci series are:", tuple(lst))


#2
print()
print("#2")
tup = ()
a = 0
b = 1
c = 0
tup=tup+(a,)
tup=tup+(b,)
for i in range(7):
    c = a + b
    a = b
    b = c
    tup=tup+(c,)
print("9 terms of Fibonacci series are:", tup)

