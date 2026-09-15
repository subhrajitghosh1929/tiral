#1
a,b,c=5,10,7
b,c,a=a+1,b+2,c-1
print(a,b,c)
#2
a=b=c=10
print(a,b,c)
#3
x=0          #variable x is created 
print(x)
#4
x=10
print(x)
x="hello world"
print(x)
#5
d=10
print(type(a))
d=20.5
print(type(d))
d="hello"
print(type(d))
#6
p=3j
q=p+(1+1.5j)
print(p)
print(q)
#7
r=2.5+3.9j
print(r.real)
print(r.imag)
#8
print('abc')
print('\\')
print("\ab")
print("seema\'s pen")
print("any's")

#9
print(0o14) #octal '14' will print equivalent decimal value which is 12
#10
print(0xC)#hexa demimal 'C' will print equivalent decimal value which is 12
#11
age=4   #float(input(" what is your age?"))
print(age)
print(3.141*(age*age))
print("I\'m",12+5,"years old")
#appendix
w,x,y,z=2,1,"one",'1'
print(y+z)
print(print())
print(print("hello"))
#print(input("enter the name:"))        #remove the # from the bigening of this line
#print(w=w+x)       #assingmemt cannot be performed with in print statement(it give an error)
#12
print("my","name","is","subhrajit",sep='?')
a,b=10,20
print("a=",a,end=' ')
print("b=",b)
#13
num=13
print(id(num))
num=num+3
print(id(num))
num=num-3
print(id(num))
num="hello"
print(id(num))
# hw q1
print("Why is 6 afraid of 7?")
input("Press Enter")
print("Because 7 8(ate) 9 :-)")
#2
day = int(input("Enter day part of today's date: "))
totalDays = int(input("Enter total number of days in this month: "))
daysLeft = totalDays - day
print(daysLeft, "days are left in current month")
#3
a = 5
print(a)
a = a * 2
print(a)
a = a - 1
print(a)
#4
a = 5
print(a, end='@')
a = a * 2
print(a, end='@')
a = a - 1
print(a)
#5
a = int(input("Enter a number: "))
b, c, d, e = a * 2, a * 3, a * 4, a * 5
print(a, b, c, d, e)
#6
r = float(input("Enter radius of circle: "))
a = 3.141* r * r
print("Area of circle =", a)
#7
m1 = int(input("Enter first subject marks: "))
m2 = int(input("Enter second subject marks: "))
m3 = int(input("Enter third subject marks: "))
m4 = int(input("Enter fourth subject marks: "))
m5 = int(input("Enter fifth subject marks: "))
avg = (m1 + m2+ m3+ m4 + m5) / 5;
print("Average Marks =", avg)
#8
ht = int(input("Enter your height in centimeters: "))
htInInch = ht / 2.54;
feet = htInInch // 12;
inch = htInInch % 12;
print("Your height is", feet, "feet and", inch, "inches")
#9
n = int(input("Enter n: "))
n2, n3, n4 = n ** 2, n ** 3, n ** 4
print("n =", n)
print("n^2 =", n2)
print("n^3 =", n3)
print("n^4 =", n4)
#10
h = float(input("Enter height of the triangle: "))
b = float(input("Enter base of the triangle: "))
area = 0.5 * b * h
print("Area of triangle = ", area)
#11
p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = int(input("Enter time: "))
si = (p * r * t) / 100
ci = p * ((1 + (r / 100 ))** t) - p
print("Simple interest = ", si)
print("Compound interest = ", ci)
#12
n = int(input("Enter number: "))
print("First five multiples of", n, "are")
print(n, n * 2, n * 3, n * 4, n * 5)
#13
n = input("Enter name of student: ")
c = int(input("Enter class of student: "))
a = int(input("Enter age of student: "))
print("Name:", n, "Class:", c, "Age:", a)
print()
print()
print("Name:", n)
print("Class:", c)
print("Age:", a)
#14
d = int(input("Enter a digit in range 1-7: "))
n = d * 10 + d + 1
n = n * 10 + d + 2
print("3 digit number =", n)
#15
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print("The three number are", a, b, c)
a, b = a + b, b + c
print("Numbers after swapping are", a, b, c)

