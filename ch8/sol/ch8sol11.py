num=int(input("enter an integer(>1000)  the last digit must not be 0 :")) 
tnum= num
reverse=0
while tnum:
    digit = tnum%10
    tnum=int(tnum/10)
    reverse= reverse*10+digit
print("Reverse  of",num,"is",reverse)
    
