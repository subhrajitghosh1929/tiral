myl=[2,4,6]
print("Existing list is :",myl)
n=eval(input("enter a number or a list to be appended:"))
if type(n)==type([]):
    print("you have accepted a list element")
    myl.extend(n)
elif type(n)==type(1):      # 1 stands for int
    print("you have accepted a int")
    myl.append(n)
else:
    print(" Please enter either an integer or a list.")# for a SET    
print("appended list is:",myl)
