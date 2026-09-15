n=int(input("enter the N.O. of rows"))
for i in range(0,n):
    for j in range (0,i+1):
        if j== 0 or j==i:
            print("*",end="")
        else:
            print(" ",end="") 
    print()
              
for i in range(n,-1,-1):
    for j in range(0,i+1):
        if j== 0 or j==i:
            print("*",end="")
        else:
            print(" ",end="")
    print() 
