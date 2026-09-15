tup=eval(input("Enter tuple :"))
mx= max(tup)
if tup.count(mx)>1:
    print("contains multiple maximum element")
else:
    print("contains only one maximum element")
