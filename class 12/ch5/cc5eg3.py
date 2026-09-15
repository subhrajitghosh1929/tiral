count = int(input("How many students are there in class? "))
fileout = open("Marks.txt", "w")
for i in range(count):
    print(f"Enter the details for student {i+1}")
    rollno = input("Roll no.: ")
    name = input("Name: ")
    marks = float(input("Marks: "))
    rec = f"{rollno},{name},{marks}\n"
    fileout.write(rec)

fileout.close()
