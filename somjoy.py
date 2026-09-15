n=int(input("How many students??? "))
if n!=0:
    d={}
print("Enter their details..")
for i in range(n):
     r=int(input("Enter roll number:  "))
     n=input("Enter name: ")
     p=float(input("Enter marks percentage: "))
     d[r]=(n,p)
     print("------------------------")
x=int(input("Enter the roll number of the student: "))
h=int(input("enter the last roll:"))
if x in d.keys( ):
    print("Details Found!")
    print("Name:",d[1][0])
    print("Marks Obtained: ",d[1][-1],"%",sep="")
    print("Name:",d[h][0])
    print("Marks Obtained:",d[h][-1],"%",sep="")
else:
 print("Not present.")
