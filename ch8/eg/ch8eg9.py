ch=input("enter a single character: ")
if ch>='A' and ch<='Z':
    print(" It is a capital letter")
elif ch>='a' and ch<='z':
    print(" It is a small letter")
elif ch>='0' and ch<='9':
    print(" It is a digit")
elif ch==' ' :
    print(" It is a space ")
else:
    print("It is a special character")
