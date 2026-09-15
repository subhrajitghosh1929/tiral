D1 = eval(input("Enter a dictionary D1: "))
print("D1 =", D1) 
D2 = {}
for key in D1:
      num = sum(D1[key])
      D2[key] = num
print(D2)
