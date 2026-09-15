# to check if there duplicate elements in  tuple or not 
tup=eval(input("enter a tuple :"))
for el in tup:
    if tup.count(el)>1:
        print("contains duplicate elements")
        break
else:
    print("does not contain duplicate elements")
