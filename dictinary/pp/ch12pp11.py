d1 = eval(input("Enter a dictionary d1: "))
d2 = eval(input("Enter a dictionary d2: "))
print("d1 =", d1) 
print("d2 =", d2)

if len(d1) > len(d2):
    longDict = d1
    shortDict = d2
else:
    longDict = d2
    shortDict = d1
for key in shortDict:
      if key in longDict:
            if longDict[key] != shortDict[key]:
                  print("d1 and d2 are different ") 
                  break
      else:
            print("d1 and d2 are different ") 
            break
else:
      print(shortDict, "is contained in", longDict)
