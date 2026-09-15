#1
print("#1")
for a in range (3):
    for b in range (5,7):
        print ("*",end='')
    print()

#2
print("#2")
for num in range (15,25):
    for i in range (2,num):
        if num%1==0:
            j=num/i
            print("founded a factori(",i,")for",num)
            break
        else:
            print(num,"is a prime number")
