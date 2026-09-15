add=input("enter text :")
i=0
ln=len(add)
while i <ln:
    ch=add[i]
    if ch.isdigit():
        sub=add[i:(i+6)]
        if sub.isdigit():
            print(sub)
            break
    i+=1
