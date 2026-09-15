a =  eval(input("Enter a list of string = "))
for i in range (len(a)):
    for j in range(len(a)-1):
        if len(a [ j ] ) > len(a [ j + 1 ]) :
            a [ j ] , a [ j + 1 ] = a [ j + 1 ] , a [ j ]
print(a)
