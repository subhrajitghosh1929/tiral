l = eval(input("Enter list of no.: "))
large = l[0]
for i in range(len(l)):
    if l[i] >= large:
        large = l[i]
for i in range(len(l)):
    if l[i] == large :
        print("Largest no at index position: ",i)
