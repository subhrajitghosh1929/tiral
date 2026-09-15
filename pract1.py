n = int(input("Enter number of students: "))
students = {}
for i in range(n):
    rollNo = int(input("Enter roll number: "))
    name = input("Enter name: ")
    percentage = float(input("Enter percentage: "))
    students[rollNo] = {'rollNo': rollNo, 'name': name, 'percentage': percentage}

first_student = students[min(students.keys())]
last_student = students[max(students.keys())]

print("First and last student:")
print("First student: Roll No - {}, Name - {}, Percentage - {:.2f}".format(first_student['rollNo'], first_student['name'], first_student['percentage']))
print("Last student: Roll No - {}, Name - {}, Percentage - {:.2f}".format(last_student['rollNo'], last_student['name'], last_student['percentage']))
