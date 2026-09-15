s1=input("enter string1: ")
s2=input("enter string2: ")
print("original string:",s1,s2)
if s1 in s2:
    s3=s2[0:4]+"restore"
print("final string:",s1,s3)
