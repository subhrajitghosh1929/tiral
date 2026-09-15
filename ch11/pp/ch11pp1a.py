# Fibonacci series using 2 variable only 
a = 0
b = 1
print(a,b,end=" ")
for i in range(7):
    b = a + b
    print(b,end=" ")
    a=b-a

#2
print()
print("#2")
a = 0
b = 1
lst=[a,b]
for i in range(7):
    b = a + b
    lst.append(b)
    a=b-a
print("9 terms of Fibonacci series are:", lst)

#3
print()
print("#3")
a = 0
b = 1
lst=[a,b]
for i in range(7):
    b = a + b
    lst.append(b)
    a=b-a
print("9 terms of Fibonacci series are:", tuple(lst))
