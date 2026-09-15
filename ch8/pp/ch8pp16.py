n = int(input("How many numbers you want to enter? "))
if n > 1 :
    l = int(input())   
    sl = int(input())
    if sl > l :
        t = sl
        sl = l
        l = t
    for i in range(n - 2) :
        a = int(input())
        if a > l :
            sl = l
            l = a
        elif a > sl :
            sl = a
    print("Second Largest Number =", sl)
else :
    print("Please enter more than 1 number")
