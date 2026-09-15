m = int(input("Enter m: "))
n = int(input("Enter n: "))
for i in range(1, n) :
    if i % m == 0 :
        print(i, "is divisible by", m)
        if i % 2 == 0 :
            print(i, "is even")
        else :
            print(i, "is odd")
