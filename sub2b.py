
#1
print(type(6/4))

#2
print(type(6//3))

#3
print(type((555/222)**2))

#4
print(type((555.0/222)**2))

#5
a=False
b=True
c=False
print(b and c)
print(b or c)
print( not a and b)
print(( a and b)or not c)
print( not b and not (a or c))
print( not ((not b or not a)and c)or a) 

#6
x=3
print(x==3.0)

#7
print("Hello"<"hello")

#8
print(False and None)

#9
print(9)
print (bool(str(0)))

#10
print (bool(None))

#11
print(6==input("value1"))
print(6==int(input("value2")))

#12
a,b,c=1,1,2
d=a+b
e=1
f=1
g=2
h=e+f
print(c==d)
print(c is d)
print(g==h)
print(g is h)

#13
x="and" *(3+2)>"or" +"4"
print(x)
print("###")
#14
#a=input()
#b=int (input())
#c=a+b
#print(c)

#15
import random
r= random.randrange(100,999,5)
print(r, end=' ')
r= random.randrange(100,999,5)
print(r, end=' ')
r= random.randrange(100,999,5)
print(r)

#16
random.randrange(11,45,4)
