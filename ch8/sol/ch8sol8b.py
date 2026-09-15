#inc
small=smallest=0
for i in range(5):
    n=int(input("Enter number: "))
    if i == 0:
        small = n
        s2=n
    elif n< small:
        s2=small
        small=n
    if i == 0:
        lar = n
        l2=n
    elif n> lar:
        l2=lar
        lar=n
print("The lowest number is: ",small)
print("The second lowest number is: ",s2)
print("The largest number is: ",lar)
print("The second largest number is: ",l2)

