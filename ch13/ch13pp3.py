lst = eval(input("Enter a three digit numbers list = "))
length = len(lst)
for i in range(1,length):
    temp = lst[i]%10
    t = lst[i]
    j = i-1
    while j>=0 and temp<(lst[j]%10):
        lst[j+1] = lst[j]
        j = j -1
    lst[j+1] = t
print(lst)
