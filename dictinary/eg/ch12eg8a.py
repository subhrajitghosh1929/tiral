M={}
n=int(input("How many students?"))
for a in range(n):
    r,m=eval(input("enter Roll No.,Marks :"))
    M[r]=m
print("creating Dictionary")
print(M)
ans=input("More student ?(y/n):")
while ans=='y':
    print("Enter detail of New student")
    r,m=eval(input("enter Roll No.,Marks :"))
    M[r]=m
    ans=input("More student ?(y/n):")
print("Dictionary after adding new student")
print(M)
