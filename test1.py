
.#M={"subh":9876,"jit":2347,"ayan":9335,"rama":7435,"chanchal":6586,"asmit":7896}
M={}
n=" "
print("1. display the dict ")
print("2. add key-value ")
print("3. deleting a particular friend ")
print("4. To modify ph")
print("5. check whether the enter name is in dict. or not")
print("6. sorting")
#creating Dict
ans='y'
while ans == 'y':
    n,p=str(input("Enter the name of friends. :")),int(input("Enter the ph. number :"))
    M[n]=p
    ans=input("More student ? (y/n)")

choice = input("Enter your choice: ")
if choice == "1":
    print(" The dict is :")
    #print("name \t phon no. ")
    #while n in M:
    print(M,end='')
elif choice == "2":
    print("add key-value ")
    ans='y'
    while ans == 'y':
        print("enter details of new student")
        n,p=str(input("Enter the name of friends. :")),int(input("Enter the ph. number :"))
        M[n]=p
        ans=input("More student ? (y/n)")
    print("Dict. after adding new students")
    print(M)
elif choice == "3":
    print("deleting a particular friend ")
    n=str(input("Enter the name of friends to be deleted :"))
    if n in M:
        del M[n]
        print("roll no. ",n," deleted from the dict.")
    else:
        print("Roll no. ",n,"dees not exist ")
    print("final dict")
    print(M)
elif choice == "4":
    print("To modify ph")
    n=str(input("Enter the name of friends. :"))
    if n in M:
        M[n]=int(input("Enter the new ph. number :"))
        print(M)
    else:
        print("no such ph. no. :")
elif choice == "5":
    print("check in ")
    n=str(input("Enter the name of friends. :"))
    if n in M:
        print(n," is present in dict.")
        print("ph. no. is",M[n])
    else:
        print("is not  present in dict.")
    print("Modified dictionary")
    print(M)
elif choice == "6":
    print("sorting order names ")
    print(sorted(M.items()))
