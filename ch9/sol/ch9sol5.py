email=input("Enter your email id:")
domain='@edupillar.com'
ledo=len(domain)
lema=len(email)
sub=email[lema-ledo:]
if sub==domain:
    if ledo !=lema:
        print("It is valid  email id")
    else:
        print("this is invalid email id - contains just domain name")
else:
    print("this email id is not valid or belong to some other domain  ")
