n=int(input("How many students?"))
stu={}
for i in range(1,n+1):
    print("Enter detail of students",(i))
    rollno=int(input("Roll no. :"))
    name=input("Name :")
    marks=float(input("Marks :"))
    d={"Roll no.":rollno,"Name":name,\
       "Marks":marks}
    key="stu"+str(i)
    stu[key]=d
print("student with marks >75 are:")
for i in range(1,n+1):
    key="stu"+str(i)
    if stu[key]["Marks"]>=75:
        print(stu[key])
