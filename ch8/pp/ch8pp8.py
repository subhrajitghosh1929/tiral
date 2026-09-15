import math

n = int(input("Enter a number: "))
sr = math.sqrt(n)
c = 0

for i in range(1, int(sr + 1)) :
    if (sr % i == 0) :
        c += 1

if c == 2 :
    print("Square root is prime")
else :
    print("Square root is not prime")
