val=eval(input("enter a list:"))
alist=[]
s=len(val)
for i in range(s):
    num=val[i]
    csum=0
    while num:
        dig=num%10
        csum+=(dig*dig*dig)
        num=num//10
    if csum==val[i]:
        print(alist.append(val[i]))
#print("largest number(sum of its digits):",max(alist))
#print("smallest number(sum of its digits):",min(alist))
