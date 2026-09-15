n = int(input("Enter a number greater than 20: "))
if n <= 20 :
    print("Invalid Input")
else :
    for i in range(11, n + 1) :
        print(i)
        if i % 3 == 0 and i % 7 == 0 :
            print("TipsyTopsy")
        elif i % 3 == 0 :
            print("Tipsy")
        elif i % 7 == 0 :
            print("Topsy")
