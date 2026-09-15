for n in range(5):
    x=int(input("Enter a number"))
    T=(x,x**2,x**3,x**4)
    for m in range(4):
        print(x,"rised to power ",m+1," is ",T[m])
