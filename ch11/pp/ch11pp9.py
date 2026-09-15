tup = ()
for i in range(1,51):
    tup = tup + (i**2,)
print("The square of integers from 1 to 50 is:" ,tup)

#b
print()
tup = ()
for i in range(1, 27):
    tup = tup + (chr(i + 96)* i,)
print(tup)
