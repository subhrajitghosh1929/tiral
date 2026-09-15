#1
print()
print("#1")
a=2
while True:         #while True;    (boolean literal) creates an infinite loop
    print(a)
    a*=2
    if a>100:       # to break the infinite looping 
        break
    


#2
print()
print("#2")
#a=b=c=0
for i in range(1,5):
    print("enter two numbers")
    a=int(input("enter the number 1 :"))
    b=int(input("enter the number 2 :"))
    if b==0:
        print("\n the denominator cannot be zero . enter again!")
        continue
    
    c=a//b
    print("Question=",c)
        
