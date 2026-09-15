print("Enter numbers:")
print("(Enter 'q' to see the result)")

l = input()

if l != 'q' and l != 'Q' :
    l = int(l)
    while True:
        n = input()
        if n == 'q' or n == 'Q' :
            break
        n = int(n)
        if n > l :
            l = n
    print("Largest Number =", l)
