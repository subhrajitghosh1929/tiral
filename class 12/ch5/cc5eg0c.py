with open("Student.txt", "w") as fileout:
    for i in range(5):
        name = input("Enter the student name: ")
        fileout.write(f"{name}\n")

