l1 = eval(input("Enter a list of strings: "))
l2 = []
for i in range(len(l1)):
    l2.append(l1[i][1:])
print("List after removing first characters:")
print(l2)
