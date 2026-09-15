num_of_students = 5
tup = ()
for i in range(num_of_students):
    print("Enter the marks of student", i + 1)
    m1 = int(input("Enter marks in first subject: "))
    m2 = int(input("Enter marks in second subject: "))
    m3 = int(input("Enter marks in third subject: "))
    tup = tup + ((m1, m2, m3),)
    print()
print("Nested tuple of student data is:", tup)
