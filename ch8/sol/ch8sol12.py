num=int(input("Enter an intger: "))
mid=num//2
print("the factor of  ", num," other than 1 and itself are:" )
for a in range(2,mid+1):
    if num%a==0:
        print(a,end=' ')
else:
    print("-End-")
