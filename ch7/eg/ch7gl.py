
#1
print("=#1")
print(0==(1==2))        # explained in the last 2 line of #1
print(2+(3==4)+5==7)
print((1<-1)==(3>4))
print(0==(1==2))
print(0==False)         # int 0 = False (False in int is 0)
print(0)
#2
print()
print("#2")
num1=4
num2=3
num3=2
num1+=num2+num3
print(num1)
num1=4
num1=num1**(num2+num3)
print(num1)
num1=4
num1**=num2+num3
print(num1)
num1='5'+'5'
print(num1)
print(4.00/(2.0+2.0))
num1=2+9*((3*12)-8)/10
print(num1)
num1=24//4//2
print(num1)
num1=float(10)
print(num1)
#num1=int('3f14')    # the str has to be like an int then only it can convert into int 
#print(num1)

num1=('Bye'=='BYE')
print(num1)
#print((10!=9 and 20>=20))
print(10+6*2**2!=9/4-3 and 29>=29/9)
print(5%10+10<50 and 29<=29)
print((0<6)or (not(10==6)and(10<0)))

#3
print()
print("#3")
#num1=25;num2=0;num1/num2 # num1/num2 it will give runtime error
bp_c=100
fp_c=0
degree=u'\N{DEGREE SIGN}'       # u\ is a unicode, we need to use {} pg-218
bp_f=(bp_c*9/5)+32
fp_f=(fp_c*9/5)+32
print("boiling point in",degree+"C:",bp_c,"and in",degree+"F:",bp_f)
print("freezing point in",degree+"C:",fp_c,"and in",degree+"F:",fp_f)

#4
print()
print("#4")
p=float(input("Enter money lent:"))
r=float(input("Enter rate of interest:"))
t=float(input("Enter time in year:"))
si=(p*r*t)/100
amount_payable=p+si
print("interest is:Rs",si)
print("amount payable is:Rs",amount_payable)

#5
print()
print("#5")
n=int(input("how many time"))
print("GOOD MORNING"*n)

#6
print()
print("#6")
import math
m=float(input("enter the mass :"))
c=3*pow(10,8)
e=m*c*c
print("equivalent energy :", e,"Joule")

#7
print()
print("#7")
import math
length=float(input("enter the length of the ladder :"))
angle=float(input("enter the angle of leaning :"))
ang_radint=math.radians(angle)
height=length*math.sin(ang_radint)
print("ladder's height on the wall:",height)
