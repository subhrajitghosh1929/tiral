strg=input("Enter a string:")
stlst=strg.split(' ')
for word in stlst:
    print(word,"(",len(word),")")
