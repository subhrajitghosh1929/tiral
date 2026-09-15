tup=eval(input("Enter a tuple :"))
ln=len(tup)
mid=ln//2
if ln%2 ==1:
    mid=mid+1
half =tup[:mid]
if sorted(half)==list(tup[:mid]):
    print("First half is sorted")
else:
     print("First half is not sorted")
