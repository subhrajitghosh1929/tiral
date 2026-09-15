# Accept student details and print the first and last student according to roll number
students = []

# Accept the number of students with error handling
while True:
    num_students = input("Enter the number of students: ")
    if num_students.isdigit() and int(num_students) > 0:
        break
    else:
        print("Please enter a positive integer greater than 0.")

num_students = int(num_students)

# Accept details of each student
for i in range(num_students):
    name = input("Enter name of student {}: ".format(i + 1))

    # Accept percentage of marks with error handling
    while True:
        percentage = input("Enter percentage of marks for {}: ".format(name))
        if percentage.replace('.', '', 1).isdigit() and 0 <= float(percentage) <= 100:
            percentage = float(percentage)
            break
        else:
            print("Please enter a valid percentage between 0 and 100.")

    # Accept roll number with error handling
    while True:
        roll_no = input("Enter roll number for {}: ".format(name))
        if roll_no.isdigit() and int(roll_no) > 0:
            roll_no = int(roll_no)
            break
        else:
            print("Please enter a positive integer greater than 0.")

    # Append student details as a tuple to the list of students
    students.append((name, percentage, roll_no))

# Sort the list of students based on roll number
from operator import itemgetter
students.sort(key=itemgetter(2))

# Print the details of the first student
print("\nFirst student details:")
print("Name:", students[0][0])
print("Percentage of marks:", students[0][1])
print("Roll number:", students[0][2])

# Print the details of the last student
print("\nLast student details:")
print("Name:", students[-1][0])
print("Percentage of marks:", students[-1][1])
print("Roll number:", students[-1][2])
