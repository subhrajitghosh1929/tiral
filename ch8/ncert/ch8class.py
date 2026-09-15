#1
for r in range (0,11,1):
 print (r)
#2
print()
print("#2")
s=0
for r in range (0,11,1):
 s=s+2
 print (s)

#3
print()
print("#3")
for i in range (1,5,1):
    for j in range (1,i+1,1):
        print("*",end=" ")
    print()
#4
print()
print("#4")
for i in range (5,0,-1):
    for j in range (1,i+1,1):
        print("*",end=" ")
    print()

#5
print()
print("#5")
s=1
for r in range (1,4):
    k=s
    for c in range (1,6):
        print(k,end=" ")
        k=k+2
        print()
    s=s+1
    print()
        
