str = input("Enter a string: ")
words = str.split()
for w in words :
    rw = ""
    for ch in w :
        rw = ch + rw
    print(rw,end=" ")
