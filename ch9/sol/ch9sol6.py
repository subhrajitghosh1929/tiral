s=input("enter some text:")
c=input("enter a character:")
print("in",s,"character",c,"found at this location:",end="")
for i in range(len(s)):
    if s[i]==c: print(i,end=",")
