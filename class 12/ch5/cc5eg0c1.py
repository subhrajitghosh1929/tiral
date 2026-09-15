fileout=open("Student.txt","w")
List1=[]
for i in range(5):
    name=input("Enter the student name: ")
    List1.append(name+'\n')
fileout.writelines(List1)
fileout.close()
