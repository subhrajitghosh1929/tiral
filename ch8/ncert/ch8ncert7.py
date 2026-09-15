num=int(input("enter the number "))
ssum=0
nnum=num
while (nnum!=0):
    digit=nnum%10
    nnum=nnum//10
    ssum+=digit
print("sum of digital of number",num,"is:",ssum)
