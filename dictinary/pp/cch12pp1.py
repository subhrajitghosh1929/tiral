d = {}
ans = "y"
while ans == "y" or ans == "Y" :
      name = input("Enter employee name: ")
      sal = float(input("Enter employee salary: "))
      d[name] = sal
      ans = input("Do you want to enter more employee names? (y/n)")    
print(d)
