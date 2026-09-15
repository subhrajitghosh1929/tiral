# type c data handling
#pg-220
#8
x = int(input("Enter a three digit number: "))
d1 = x % 10
x //= 10
d2 = x % 10
x //= 10
d3 = x % 10
y = d1 * 100 + d2 * 10 + d3
print("Reversed Number:", y)
