string=input("Enter the string: ")
string=" "+string.strip()
a=0
string2=''
while a <len(string):
    if string[a]==' ' and string[a+1]!='':
        string2+=string[a]+string[a+1].upper()
        a+=1
    else:
        string2+=string[a]
    a+=1
print("original string:",string)
print("capitalized word string:",string2)
