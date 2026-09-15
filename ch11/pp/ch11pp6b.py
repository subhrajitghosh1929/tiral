num_of_students = 5
tup = ()
tup1=()
for i in range(num_of_students):
    print("Enter the marks of student", i + 1)
    m1 = int(input("Enter marks in first subject: "))
    m2 = int(input("Enter marks in second subject: "))
    m3 = int(input("Enter marks in third subject: "))
    s=(m1,m2,m3)
    tup = tup + (s,)
    s1=sum(s)
    tup1+=(s1,)
print()
print("Nested tuple of student data is:", tup)
print()
for i in range(num_of_students):
    print("elemens of tuple ",i+1," ",tup[i])
    print()
print()
for i in range(num_of_students):
    print("total of student ",i," is ",tup1[i])
    print("average of student ",i," is ",tup1[i]/len(s))
    print()
