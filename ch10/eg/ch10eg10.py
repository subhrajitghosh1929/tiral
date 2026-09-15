lst=eval(input("Enter a list:"))
length=len(lst)
mean=sum=0
for i in range(0,length):
    sum+=lst[i]
mean=sum/length
print("given list is:",lst)
print("the mean of given list is :",mean)
