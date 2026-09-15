def nthRoot(x, n = 2):
    return x ** (1/n)

x = int(input("Enter the value of x:"))
n = int(input("Enter the value of n:"))

result = nthRoot(x, n)
print("The", n, "th root of", x, "is:", result)

default_result = nthRoot(x)
print("The square root of", x, "is:", default_result)
