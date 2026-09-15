#to sort a list using inserting sort in decending order
a=[15,6,13,22,3,52,2]
print ("Original list is: ",a)
n=len(a)
for i in range(1,n):
    key=a[i]
    j=i-1
    while j>=0 and key > a[j]:
        a[j+1]=a[j]
        j=j-1
    else:
        a[j+1]=key
print("The sorted list is: ",a)
