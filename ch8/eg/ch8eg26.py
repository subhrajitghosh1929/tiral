#1
print()
print("#1")
for a in range(1,4):
 if a%2==0:
    break
 print("Element is ",end=' ')
 print(a)
else:
    print("ending loop after printing all elements of sequence")

#2
print()
print("#2")
for a in range(1,4):
    print("Element is ",end=' ')
    print(a)
    if a%2==0:
        break
    else:
        print("ending loop after printing all elements of sequence")

#3
print()
print("#3")
count=sum=0
ans='y'
while ans=='y':
    num=int(input("enter the number :"))
    if num<0:
        print("number entered is below zero. Aborting!")
        break
    sum=sum+num
    count=count+1
    ans=input("want to enter more number? (y/n)")
else:
    print("you entered",count,"number so far")
print("sum of number entered is",sum)

