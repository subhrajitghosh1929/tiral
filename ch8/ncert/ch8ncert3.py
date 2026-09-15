for i in range(5):
    n=int(input("Enter number: "))
    if i == 0:
        small = n
    elif n< small:
        small=n
    if i == 0:
        lar = n
    elif n> lar:
        lar=n
print("The lowest number is: ",small)
print("The largest number is: ",lar)


