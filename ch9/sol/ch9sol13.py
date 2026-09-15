s=input("enter a string:")
test=False
dig="0123456789"
for ch in s:
    if ch in dig:
        print("the string contain a digit")
        test=True
        break
else:
    test==False
    print("the string doesn't contain a digit")
