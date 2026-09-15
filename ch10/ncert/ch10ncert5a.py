val1=eval(input("enter a list :"))
val1.sort()
print(val1)
s=len(val1)
mid=s//2
print(mid)
if s%2==0:
     med= val1[mid]
     print("med of the given list is :",med)
else:
    m1,m2=mid,mid+1
    med=(val1[m1]+val1[m2])/2
    print("median of the given list is :",med)
