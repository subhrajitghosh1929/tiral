str = input("Enter a string: ")+" "
rw=""
for w in range(len(str)):
    if str[w]==" " : 
        print(rw,end=" ")
        rw=""
    else:
        rw=str[w]+rw
