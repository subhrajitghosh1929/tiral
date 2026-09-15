num= int(input("enter 3 digit number:"))
summ=0
temp=num
while (temp>0):
    digit =temp%10
    summ+=digit**3
    temp//=10
if (num==summ):
    print(num,"is an armstrong number :")
else:
    print(num,"is not an armstrong number :")
