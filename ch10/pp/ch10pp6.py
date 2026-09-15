ln=eval(input("Enter a list : "))
ele=eval(input("Enter the element to be searched : "))
l=len(ln)
#for i in range(l):
print(ele is ln)
if ele in ln  :
    print("the element is present in the list : ")
else:
    print("the element is not present in the list : ")
