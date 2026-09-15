#1
print("#1")
x=eval("5+8")
y=eval("3*10") 
print(x)
print(y)


#2
print()
print("#2")
var1=eval(input("Enter a value:"))
print(var1,type(var1))


#3
print()
print("#3")
var1=list(input("Enter a value:"))
print(var1,type(var1))

#4
print()
print("#4")
l=list()
print(l)

#5
print()
print("#5")
l1=[3,4,[5,6],7]
print(l1[2][1])

#6
print()
print("#6")
l1=[3,4,[5,6],7]
print(l1[2])        #'tuple' object is not callable


#7
print()
print("#7")
var1=tuple(input("Enter a value:"))
print(var1,type(var1))

#8
print()
print("#8")
var1=list(input("Enter a value:"))
var2=var1[2:5]
print(var1[2:5])
print(var2)

#9
print()
print("#9")
var1=tuple(input("Enter a value:"))
print(var1[2:5])

#10
print()
print("#10")
var1=list(input("Enter a value:"))
print(len(var1))


#11
print()
print("#11")
var1=list(input("Enter a value:"))
print(len(var1[2:5]))

#12
print()
print("#12")
var1=list(input("Enter a value:"))
#print('2' in(var1[2:5]))
print(var1[2]+var1[5]*5)

#13
print()
print("#13")
r=input("enter a string :")
for a in r:
    print(a)

