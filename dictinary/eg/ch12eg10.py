n=int(input("How many student ?"))
cw={}
for a in range(n):
    keys=input("name of the student :")
    value=int(input("Number of compition won :"))
    cw[keys]=value
print("The dictionary now is :")
print(cw)
