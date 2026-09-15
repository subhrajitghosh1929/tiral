#inc
small=smallest=0
for i in range(5):
    n=int(input("Enter number: "))
    if i == 0:
        small = n
    elif n< small:
        small=n
"""for i in range(5):
    n=int(input("Enter number: "))
    if n< small:
        pass
    else:
        small=n"""
print("The lowest number is: ",small)
#print("The second lowest number is: ",small)

