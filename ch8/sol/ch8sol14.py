x=int(input("enter a positive number: "))
n=int(input("enter a power(n): "))
power=1
for r in range(n):
    power=power*x
print(x,"to the power",n,"is",power)
