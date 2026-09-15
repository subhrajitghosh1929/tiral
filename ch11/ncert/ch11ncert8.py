lst =[]
n=int(input("how many student?"))
for i in range(1, n+1):
    email = input("Enter email id of student" + str(1) +"; ")
    lst.append(email)
    etuple=tuple(lst)
lst1=[]
lst2=[]
for i in range(n) :
    email = etuple[i].split("@")
    lst1.append(email[0])
    lst2.append(email[1])
    unameTup=tuple(lst1)
    dnameTup=tuple(lst2)
print("Student all")
print(etuple)
print("user name tuple :")
print (unameTup)
print("Domain name tuple")
print(dnameTup)

#abc@xyz.net
#
#myname@school.com
#xyz@abc.com
