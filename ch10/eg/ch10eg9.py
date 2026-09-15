lst=eval(input("enter list:"))
length=len(lst)
min_ele=lst[0]
min_index=0
for i in range(1,length):
    if lst[i] < min_ele:
        min_ele=lst[i]
        min_index=i
print("Given list is:",lst)
print("the minimum element of the given list is:")
print(min_ele,"at index",min_index)
