n=int(input("Enter number: "))
summ=0
for i in range(1,n):
    if (n%i==0):
        summ=summ+i
if (summ==n):
    print("the number ",n,"is a perfect number!")
else:
    print("the number",n,"is not a perfect number!")
