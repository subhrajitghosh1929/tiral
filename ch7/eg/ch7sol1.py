#1
print("#1")
print(type(3))
print(type(3j))
print(type(13.0))
print(type('13'))
print(type("13"))
print(type(2+0j))
print(type(13))
print(type([3,13]))
print(type((3,13)))

#2
print()
print("#2")
print(len(str(17//4)))
print(str(17/3))
print(len(str(17/3)))

#3
print()
print("#3")
print(12/4)
print(14//14)
print(14%4)
print(14.0/4)
print(14.0//4)
print(14.0%4)
input
#4
print()
print("#4")
dk= str(input("enter name:"))
print("Name is ; ",dk )

#5
print()
print("#5")
print(5<5 or 10)    #Ln1  it will evaluate 2nd one as the 1st expression is false  hence it will evaluate to 10

print(5<10 or 5)  #Ln2     when 5 is <10 then it gives true  as the 1st is true  hence it will not evaluate 2nd one

print(5>10 or 5)  #Ln3     when 5 is >10 then it gives 5    as the 1st expression is false hence it will evaluate 2nd one

print(5<(10 or 5))  #Ln4  in case of () it will take 10 which  = true(as the expression is true)  it will  evaluate true (in case of or)
                                                                                                      
print(5<(0 or 5))  #Ln5  in case of () it will take 0 which = false 5<5(2nd value) which is false then it will evaluate to false

print(5>(10 or 5))  #Ln6  in case of () it will take 10 then it will evaluate > relational operator which is false hence it will return false

print(5<(10 and 5))  #Ln7  in case of () it will take 5(and take 2nd one) then it will  evaluate < hence False

print(5<(5 or 10))   #Ln8  in case of () it will take 5(or take 1st one) then it will evaluate < hence False

                    # in Ln4,5,6&7 boolean value supersedes int value in case of relational operator  

#6
print()
print("#6")
a=5
b=-3
c=25
d=-10
print(a+b+c>a+c-b*d)
print(str(a+b+c>a+c-b*d)== "true")
print(len(str(a+b+c>a+c-b*d))== len(str(bool(1))))

#7
print()
print("#7")
a=3+5/8
b=int(3+5/8)
c=3+float(5/8)
d=3+float(5)/8
e=3+5.0/8
f=int(3+5.0/8)
print(a,b,c,d,e,f)

#8
print()
print("#8")
print(87//5)
print(87//5.0)
print(bool (87//5.0)==(87//5))
print(bool(87//5.0)==int(87/5))
print(bool(87//int (5.0))==(87//5.0))

#9
print()
print("#9")
print(17%5)
print(17%5.0)
print((17%5)==(17%5))
print((17%5)is(17%5))
print((17%5.0)==(17%5.0))
print((17%5.0)is(17%5.0))
print()
print("write the output of the following")
print(17%5)==(17%5)     #it wiil ignore from  ==
print(17%5)is(17%5)     #it wiil ignore from  is
print(17%5.0)==(17%5.0) #it wiil ignore from  ==
print(17%5.0)is(17%5.0) #it wiil ignore from  is

#10
print()
print("#10")
import math
print(math.pow(--5,2))
 
#11
print()
print("#11")
print(bool(0))
print(bool(1))
print(bool('0'))
print(bool('1'))
print(bool(""))         #there is no space in between if space then true 
print(bool(0.0))
print(bool('0.0'))
print(bool(0j))         #as because there is zero otherwise true
print(bool('0j'))
print(bool(1j))
#12
print()
print("#12")
print(bool(int('0')))       # for int and float false
print(bool(str(0)))
print(bool(float('0.0')))   # for int and float false
print(bool(str(0.0)))

#13
print()
print("#13")
print(13 or len(13))
#print(len(13) or 13)  #len work on string only incase of OR operator 1st is executed only

#14
print()
print("#14")
import random
print(15+random.random()*5) # after learning ch 8 use loop

#15
print()
print("#15")
l=float(input("enter base/length of the parallelogram:"))
w=float(input("enter width of the parallelogram:"))
h=float(input("enter height of the parallelogram:"))
area=l*h
perimeter=2*l+2*w
print("the area of given the parallelogram:",area)
print("the perimeter of given the parallelogram:",perimeter)

#16
print()
print("#16")
print(bool(int('0')))
print(bool(str(0)))
print(bool(float('0.0')))
print(bool(str(0.0)))

#17
print()
print("#17")
import random
student1=random.randint(1,100)      # after learning ch 8 use loop
student2=random.randint(1,100)      # ( then only one statement would be required)
student3=random.randint(1,100)
print("3 choose student are",)
print(student1,student2,student3)

#18
print()
print("#18")
import math
a,b,c=17,23,30
s=(a+b+c)/2
area=math.sqrt(s *(s-a)* (s-b) *(s-c))
print("sides of triangle :",a,b,c)
print("area:",area,"units square")
