string=input("Enter the string: ")
length=len(string)
a=0
string2=''
while a <length:
    if a==0:
        string2+=string[0].upper()
        a+=1
    elif string[a]==' ' and string[a+1]!='':
        string2+=string[a]
        string2+=string[a+1].upper()
        a+=2
    else:
        string2+=string[a]
        a+=1
print("original string:",string)
print("capitalized word string:",string2)
