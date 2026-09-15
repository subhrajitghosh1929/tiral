l = eval(input("Enter list: "))
n = int(input("Enter number to search: "))
if n in l:
    print(n, "found at index", l.index(n))
else :
    print(n, "not found in list")
