n = 10
details = {}
for i in range(n):
    name = input("Enter the name of student: ")
    roll_num = int(input("Enter the roll number of student: "))
    marks = int(input("Enter the marks of student: "))
    grade = input("Enter the grade of student: ")
    details[roll_num] = [name, marks, grade]
    print()
print(details)
