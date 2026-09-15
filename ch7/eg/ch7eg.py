#1
print("#1")
x,z=5,10
y=x+3
x=x-1
x=x+z
print('x:',x,'y:',y,'z:',z)

#2
print()
print("#2")
print(14//4,14%4,14/4)

#3
print()
print("#3")
print(2*'no'+3*'!')
print(2*('no'+3*'!'))

#4
print()
print("#4")
print(type(1+3))
print(type(1+3.0))

#5
print()
print("#5")
print(11+3)
print('11'+'3')
#print('11'+3) will give error as it can concatct only str and not str with int  
print()

print(type(5*2))
print(type(5**2))
print(type('5'+'2'))
print(type('5'*2))
print(type(5/2))
print(type(5//2))
print(type(5%2))
print(type(5+2.0))
print(type(5.0*2.0))
#print(type('5'-2))will give error as it does not support(-) with str
#5a
print()
print("#5a")
x,y,z,q=5,5,6,6
print(x>y)
print(y<=z)
#print(z<>x) it dosen't support <>
print(z==q)
print(x<y>z)
#print(x==y<>z) it dosen't support <>
#5b
print()
print("#5b")
a,b,c=3,4,5
print(a or b)       # or will return the 1st value (3)
print(b and c)      # and will return the 2nd value(5)
print(a and not b)   # not returns false
print(not c or not b)   # not returns false
#5c
print()
print("#5c")
ch,i,fl=5,2,4
db,fd=5.0,36.0
A=(ch+i)/db
B=fd/db*ch/2
print(A)
print(B)

#6
print()
print("#6")
a,b=3,6
c=b/a
print(c)
c=b//a
print(c)
c=b%a
print(c)

#7
print()
print("#7")
p,q,y=1,2,3
print(p>q<y)
a,N,b=1,2,3
print(a<=N<=b)

#7a
print()
print("#7a")
print(25/5 or 2.0+20/10)

#7b
print()
print("#7b")
print(a or (b and (not c)))

print((p and q)or (not r))

#7c
print()
print("#7c")
print((5<10)and (10<5) or (3<18) and not 8<18)

print((5<10) or (50<100/0))

#8
print()
print("#8")
x,y=6,3
age=21
state='Goa'
name='Subhrajit'
print(x%y==0)
print(age>=18 and state=='Goa')
print(name!='Nimra')

#9
print()
print("#9")
import math
a,b,c=3,4,5
p,q,r=7.0,9.3,10.51
x,y,z=25.519,10-24.113,231.05
print(math.pow(a/b,3.5))
print(math.sin(p/q)+math.cos(a-c))
print(x/y+math.floor(p*a/b))
print(((math.sqrt(b)*a)-c))
print(((math.ceil(p)+a)*c))

#10
print()
print("#10")
import math
a,b,c=2,3,4
x,y=30,2
p,q,r,s=3,4,1,2
print(math.sqrt(a*a+b*b+c*c))
print(2-y*math.exp(2*y)+4*y)
print(p+q/math.pow((r+s),4))
print((math.cos(x)/math.tan(x))+x)
print(math.fabs(math.exp(2)-x))
print(math.exp(4))
