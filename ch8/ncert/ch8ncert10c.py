n=int(input("enter the no of rows :"))
k=2
for i in range(n,0,-1):
    for j in range(1,k+2):
        print(end=" ")
    for j in range(1,i+1):
        print(j,end="")
    k=k+1
    print() 
