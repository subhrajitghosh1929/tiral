string=input("Enter the string: ")
string=" "+string.strip()
a=0
string2=''
for a in range(0,len(string),1):
    if string[a]==' ' and string[a+1]!='':
        string2+=string[a]+string[a+1].upper()
    elif a!=0 and string[a-1]==' ' and string[a]!='':
        string2+=''
    else:
        string2+= string[a]
print("original string:",string)
print("capitalized word string:",string2)
