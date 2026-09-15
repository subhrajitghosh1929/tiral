string=input("Enter the string: ")
string=" "+string.strip()
a=0
string2=''
for a in range(len(string)):
    if string[a]==' ' and string[a+1]!='':
        string2+=string[a]+string[a+1].upper()
    elif a!=0 and string[a-1]==' ' and string[a]!='':
        continue  
    else:
        string2+= string[a]
print("original string:",string)
print("capitalized word string:",string2)
