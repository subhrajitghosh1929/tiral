str1=input("enter a string")
uc,lc=0,0
for ch in str1:
    if ord(ch)>=65 and ord(ch)<91:
        uc+=1
    if ord(ch)>=97 and ord(ch)<123:
        lc+=1
print("no.of capital letter",uc)
print("no.of small letter",lc)
