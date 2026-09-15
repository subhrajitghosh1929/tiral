#to sort a list using bubble sort in ascending order
a=[15,6,13,22,3,52,2]
print ("Original list is: ",a)
n=len(a)
"""for i in range (n):
    for j in range (0,n-i-1):
        if a[j] > a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print("The sorted list is: ",a)"""

# Insertion sort 
for i in range (1 ,n) :
    temp = a [ i ]
    j = i - 1
    while j >=0 and temp < a[j]:
        a[j+1] = a[j]
        j = j - 1
    a[j+1] = temp
print("The sorted list is: ",a)
