M={}
n=int(input("How many student?"))
for a in range(n):
    r,m=eval(input("enter Roll no.,Mark:"))
    M[r]=m
print("creating dictionary")
print(M)
print("to modify")
r=int(input("Enter roll number :"))
if r in M:
    M[r]=float(input("enter NewMarks:"))
else:
    print("No such Roll no. is present")
print("Modify dictionary")
print(M)

"""
output
1,67.4
enter Roll no.,Mark:2,33.3
enter Roll no.,Mark:3,45.6
enter Roll no.,Mark:4,90
"""
"""
#2
print()
print("#2")
if n in M:
    M[n]=float(input("enter NewMarks:"))
else:
    print("No such Roll no. is present")
print("Modify dictionary")
print(M)

#3
print()
print("#3")
if m in M:
    M[m]=float(input("enter NewMarks:"))
else:
    print("No such Roll no. is present")
print("Modify dictionary")
print(M)
"""
