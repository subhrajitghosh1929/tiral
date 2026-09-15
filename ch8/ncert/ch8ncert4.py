yr=int(input("enter a 4-digit number :"))
if yr % 100==0:
    if yr % 400==0:
        leap=True
    else:
        leap=False
elif yr%4==0:
    leap=True
else:
    leap=False
if leap==True:
    print(yr,"is a leap years")
else:
    print(yr,"is not a leap years")
        
