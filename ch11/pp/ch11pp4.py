tup = ()
ans = "y"
while ans == "y" or ans == "Y" :
      roll_num = int(input("Enter roll number of student: "))
      name = input("Enter name of student: ")
      marks = int(input("Enter marks of student: "))
      tup += ((roll_num, name, marks),)
      ans = input("Do you want to enter more marks? (y/n): ")
print(tup)
