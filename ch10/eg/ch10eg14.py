lst=eval(input("Enter a list:"))
ln=len(lst)
mx=max(lst)
ind=lst.index(mx)
if ind<(ln/2):
    print("The maximum element",mx,"lies in the 1st half")
elif ind==(ln/2):
    print("The maximum element",mx,"lies in the middle")
else:
    print("The maximum element",mx,"lies in the 2st half")
