#1
name="python"
print(len(name))
print()
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print()
print(name[-6])
print(name[-5])
print(name[-4])
print(name[-3])
print(name[-2])
print(name[-1])

#2
print()
print("list")
a=[1,2,3,4,5]
b=['a','e','i','o','u']
c=['neha',102,79.5]
d=["a b","e f","i j","o p","u v"]
e=['''a''','''e''','''i''','''o''','''u''']
f=['''ab''','''ef''','''ij''','''op''','''ur''']
g=['''a b''','''e f''','''i j''','''o p''','''u r''']
print(a,b,c,d,e,f,g)

#3
print()
print("tuple")
a=(1,2,3,4,5)
b=('a','e','i','o','u')
c=('neha',102,79.5)
d=("a b","e f","i j","o p","u v")
e=('''a''','''e''','''i''','''o''','''u''')
f=('''ab''','''ef''','''ij''','''op''','''ur''')
g=('''a b''','''e f''','''i j''','''o p''','''u r''')
print(a,b,c,d,e,f,g)

#4
print()
print("set")
a={1,2,3,4,5}
b={'a','e','i','o','u'}
c={'neha',102,79.5}
d={"a b","e f","i j","o p","u v"}
e={'''a''','''e''','''i''','''o''','''u'''}
f={'''ab''','''ef''','''ij''','''op''','''ur'''}
g={'''a b''','''e f''','''i j''','''o p''','''u r'''}
print(a,b,c,d,e,f,g)

#5
print()
print("dictionary")
a={1:1,2:2,3:3,4:4,5:5}
b={'a':1,'e':2,'i':3,'o':4,'u':5}
c={'neha':'a',102:'b',79.5:'c'}
d={"a b":1,"e f":2,"i j":3,"o p":4,"u v":5}
e={'''a''','''e''','''i''','''o''','''u'''}
f={'''ab''','''ef''','''ij''','''op''','''ur'''}
g={'''a b''','''e f''','''i j''','''o p''','''u r'''}
print(a,b,c,d,e,f,g)
print(c['neha'])

#6
print()
p=5
q=p
r=5
print(id(5))
print(id(p))
print(id(q))
print(id(r))

#7
print()
p=10
q=r
r=7
print(id(10))
print(id(p))
print(id(q))
print(id(r))
print(id(5))

#8
print()
chk=[2,4,6]
print(chk)
print(id(chk))
chk[1]=40
print(chk)
print(id(chk))

#9
print()
a=4
print(type(4))
print(type(a))

#10
print()
print("square")
a=4
b=2
print(a**b) 
print("cube")
a=4
b=3
print(a**b)
print("sq root")
a=4
b=0.5
print(a**b)
print("cube root")
a=8
b=0.3333333333333333
print(a**b)

#11
print()
a,b,c,d=9.2,2.0,4,21
print(a/4,a//4)
print(b**c)
print(d//b)
print(a%c)

#12
print("#12")
import math
r = 3.75
a = math.pi * r **2 
print("area of Circle =",a,'sq meters')

#13
print()
print(5//-3)
print(-5//3)
print(-5/3)
print(-5%3)
print(5%-3)

#14
print()
a=3
b=13
c='n'
d='g'
e='N'
f='god'
g='God'
h='god'
j='God'
k='Godhouse'
L=[1,2,3]
M=[2,4,6]
N=[1,2,3]
O=(1,2,3)
P=(2,4,6)
Q=(1,2,3)
a<b
c<d
f<h
f==h
c==e
g==j
"God"<"Godhouse"
"god"<"Godhouse"
a==p
L==M
L==N
O==P
O==Q
print(a==True)
print(0==False)
print(1==True)

#15
print()
a=235
b=240
c=235
print(a is b)
print(a is c)
b=b-a
print(a is b)
print(id(a),id(b),id(c))
print(a,b)

#16
print()
s1='abc'
s2= input("enter a string:")
print(s1==s2)
print(s1 is s2)
s3='abc'
print(s1 is s3)

#17
print()
i=2+3.5j
j=2+3.5j
print(i is j)

#18
print()
k=3.5
l=float(input("Enter the value:"))
print(k==1)
print(k is 1)
