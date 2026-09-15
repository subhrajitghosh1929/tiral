#to find the largest string (prints the 1st
#longest string when 2 or more longest strings are there )
l = eval(input("Enter list of strings: "))
largeIdx = 0
largeLen = 0
for i in range(len(l)):
    length = len(l[i])
    if length > largeLen:
        largeLen = length
        largeIdx = i
print("Longest String:", l[largeIdx])

#to find the largest string (prints the last
#longest string when 2 or more longest strings are there )

largeIdx = 0
largeLen = 0
for i in range(len(l)):
    length = len(l[i])
    if length >= largeLen:
        largeLen = length
        largeIdx = i
print("Longest String:", l[largeIdx])

#to find the largest string (prints all
#longest strings when 2 or more LONGEST strings are there )

largeIdx = 0
largeLen = 0
for i in range(len(l)):
    length = len(l[i])
    if length >= largeLen:
        largeLen = length
        largeIdx = i
for i in range(len(l)):
    length = len(l[i])
    if length == largeLen :
        print("Longest String(s):", l[i])
