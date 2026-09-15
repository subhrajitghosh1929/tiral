D1 = eval(input("Enter a dictionary D1: "))
print("D1 =", D1) 
val = tuple(D1.values())
seen = []
flag = True
for i in val:
    if i not in seen:
        seen.append(i)
        count = val.count(i)
        if count > 1:
            print(count, "keys have same value of", i)
            flag = False
if flag:
    print("No keys have same values")
