lst=[]
n=int(input("How many student?"))
for i in range(1, n+1):
    name=input("Enter name of student "+str(1)+":")
    lst.append(name)
ntuple=tuple(lst)
nm=input("Enter name to be search for :")
if nm in ntuple:
    print(nm, "exist in the tuple")
else:
    print(nm, "does not exist in the tuple")

Anaya
Enter name of student 1:Anusha
Enter name of student 1:Kirat
Enter name of student 1:Kyle
Enter name of student 1:Suji
Enter name to be search for :Kirat
