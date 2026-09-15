str1=input("enter a string")
uc,lc=0,0
for ch in str1:
    if ch>='A' and ch<'Z':
        uc+=1
    if ch>='a' and ch<'z':
        lc+=1
print("no.of uppercase letter",uc)
print("no.of lowercase letter",lc)
