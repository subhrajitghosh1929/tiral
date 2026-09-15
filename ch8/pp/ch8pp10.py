print("First Series:")
for i in range(1, 41, 3) :
    print(i, end = ' ')

print("\nSecond Series:")
x = 1
for i in range(1, 41, 3) :
    print(i * x, end = ' ')
    x *= -1
