fileout=open("marks.txt","a")
n=int(input("enter the number of student you want to add :"))
for i in range(n):
    print("Enter the details of student",(i+1),"below:")
    rollno=int(input("Roll no."))
    name=input("Name")
    marks=float(input("Mark"))
    rec=str(rollno)+","+name+","+str(marks)+'\n'
    fileout.write(rec)
fileout.close
