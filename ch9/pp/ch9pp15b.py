str = input("Enter a string: ")+" "
rw =""
for w in str :
    if w==" " : 
        print(rw,end=" ")
        rw = ""
    else:
        rw = w + rw
