FILE : CH13eg1

#to sort a list using bubble sort in ascending order
a=[15,6,13,22,3,52,2]
print ("Original list is: ",a)
n=len(a)
for i in range (n):
    for j in range (0,n-i-1):
        if a[j] > a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print("The sorted list is: ",a)

FILE : CH13eg1a

#to sort a list using bubble sort in descending order
a=[15,6,13,22,3,52,2]
print ("Original list is: ",a)
n=len(a)
for i in range (n):
    for j in range (0,n-i-1):
        if a[j] < a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print("The sorted list is: ",a)

FILE : CH13eg1b

#to sort a list using bubble sort in ascending order
a=eval(input("enter the elements of a list in unsorted manner"))
print ("Original list is: ",a)
n=len(a)
for i in range (n):
    for j in range (0,n-i-1):
        if a[j] > a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print("The sorted list is: ",a)

FILE : CH13eg1c

#to sort a list using bubble sort in descending order
a=eval(input("enter the elements of a list in unsorted manner"))
print ("Original list is: ",a)
n=len(a)
for i in range (n):
    for j in range (0,n-i-1):
        if a[j] < a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print("The sorted list is: ",a)

FILE : CH13eg2

#to sort a list using inserting sort in ascending order
a=[15,6,13,22,3,52,2]
print ("Original list is: ",a)
n=len(a)
for i in range(1,n):
    key=a[i]
    j=i-1
    while j>=0 and key < a[j]:
        a[j+1]=a[j]
        j=j-1
    else:
        a[j+1]=key
print("The sorted list is: ",a)

FILE : CH13eg2a

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

FILE : CH13eg2b

#to sort a list using inserting sort in ascending order
a=eval(input("enter the element of the unsorted list"))
print ("Original list is: ",a)
n=len(a)
for i in range(1,n):
    key=a[i]
    j=i-1
    while j>=0 and key < a[j]:
        a[j+1]=a[j]
        j=j-1
    else:
        a[j+1]=key
print("The sorted list is: ",a)

FILE : CH13eg2c

#to sort a list using inserting sort in ascending order
a=eval(input("enter the element of the unsorted list"))
print ("Original list is: ",a)
n=len(a)
for i in range(1,n):
    key=a[i]
    j=i-1
    while j>=0 and key < a[j]:
        a[j+1]=a[j]
        j=j-1
    else:
        a[j+1]=key
print("The sorted list is: ",a)




