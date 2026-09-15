t=int(input("enter many terms? (enter 2+ value) :"))
first=0
second=1
print("\nFibonacci series is : ")
print(first,end=",")
print(second,end=",")
for i in range(2,t):
    next =first+ second
    print( end=",",next)
    first= second
    second=next
    
