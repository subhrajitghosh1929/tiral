string=input("enter a string: ")
length=len(string)
print("original string :",string)
string2=""
for a in range(0,length,2):
    string2+=string[a].upper()+string[a+1]
print("Alternatively capitalised string:",string2)
