# WAP accept a no of days(a day no) from the user and displsy in years,month,
# week, days
d=int(input(" enter a value "))
y=d//365
d=d%365
m=d//30
d=d%30
w=d//7
d=d%7
print("years=",y)
print("month=",m)
print("week=",w)
print("day=",d)
