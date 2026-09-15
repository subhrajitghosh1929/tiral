num=int(input("enter an integer(>1000): "))
tnum= num
reverse=0
for i in range(tnum,0,-1) :
    digit = tnum%10
    print(digit)
    tnum=int(tnum/10)
    reverse= reverse*10+digit
print("Reverse  of",num,"is",reverse)
    
