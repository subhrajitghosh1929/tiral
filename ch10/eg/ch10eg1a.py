#1
print()
print("#1")
a=[10,12,14]
a+="abc"            # list can be added to a string when it is a accumilator(+=)
print(a)            ###** "abc" is treated as a list and not as a string

#2
print()
print("#2")
a=[10,12,14]
#a=a+"abc"      list can't be added to a string
print(a)

#3
print()
print("#3")
a=[10,12,14,20,22,24,30,32,34] 
print(a[3:-3])

#4
print()
print("#4")
L=["one","two","three","four"]
print(L)
L[0:1]=[4,5]
print(L)
L[0:2]=[0,1]
print(L)
L[0:3]=[0,1]
print(L)
L=["one","two","three","four"]
L[0:2]="a"
print(L)
#5
print()
print("#5")
L[0:-2]=[345]
print(L)

#6
print()
print("#6")
a=[1,2,3]
a1=[1,2,3]
b=a
a[1]=5
print(a)
print(b)
a1[1]=5
b=a1
b=list(a1)
print(b)
#7
