tup=eval(input("Enter a tuple: "))
ln=len(tup)
num=tup.count(tup[0])    # counts the no. of times a particular element 
print(num)              #  is present in the tuple 'tup' 
if num==ln:
    print("Tuple contains all the same element ")
else:
    print("Tuple contains different element")
