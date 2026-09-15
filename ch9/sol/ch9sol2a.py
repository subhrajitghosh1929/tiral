string=input("enter a string:")
length=len(string)
mid=length//2
rev=-1
a=0
while a <= mid:
    if string[a]==string[rev]:
        a+=1
        rev-=1
    else:
        print(string,"is not a palidrome")
        break
else:
    print(string,"is a palidrome")
