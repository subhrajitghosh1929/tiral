M={}
n=int(input("How many students?"))
for a in range(n):
    r,m=eval(input("enter Roll No.,Marks :"))
    M[r]=m
print("creating Dictionary")
print(M)
ans='y'
while ans=='y':
    print("Enter detail of New student")
    r,m=eval(input("enter Roll No.,Marks :"))
    M[r]=m
    ans=input("More student ?(y/n):")
print("Dictionary after adding new student")
print(M)
print("Create Dictionary")
print(M)
rno=int(input("roll No. to be deleted? :"))
if rno in M:
    del M[rno]
    print("Roll no.",rno,"delete from dictonary ")
else:
    print("Roll no.",rno,"does not exist in dictonary ")
print("Final dictonary ")
print(M)
