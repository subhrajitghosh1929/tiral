sum=0
n=int(input("how many terms?"))
#added 2 to n becasuse started with 2
for a in range(2,n+2):
    t=0
    for b in range (1,a):
        t+=b
    print("Term",(a-1),":",t)
    sum+=t
print("sum of",n,"term is", sum)
