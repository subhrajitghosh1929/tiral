rno=[]
mks=[]
for a in range(4):
    r,m=eval(input("enter roll no.,Marks:"))
    rno.append(r)
    mks.append(m)
d={rno[0]:mks[0],rno[1]:mks[1],rno[2]:mks[2],rno[3]:mks[3]}
if d[2]>75:
    print("roll number 2 scored",d[2],"(>75)")
else:
    print("roll number 2 scored",d[2],"(<75)")
print("Creating dictionary")
print(d)
