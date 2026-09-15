tup = eval(input("Enter a tuple: "))
maxCount = 0
mode = 0
for i in tup :
      count = tup.count(i)
      if maxCount <  count:
            maxCount = count
            mode = i

print("mode:", mode)
