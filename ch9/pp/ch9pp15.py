str = input("Enter a string: ")
words = str.split()
newStr = ""
for w in words :
    rw = ""
    for ch in w :
        rw = ch + rw
    newStr += rw + " "
print(newStr)
