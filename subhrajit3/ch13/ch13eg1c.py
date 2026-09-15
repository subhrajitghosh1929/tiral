#to sort a list using bubble sort in descending order
a=eval(input("enter the elements of a list in unsorted manner"))
print ("Original list is: ",a)
n=len(a)
for i in range (n):
    for j in range (0,n-i-1):
        if a[j] < a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print("The sorted list is: ",a)
