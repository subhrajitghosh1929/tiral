d1 = eval(input("Enter first dictionary: "))
d2 = eval(input("Enter second dictionary: "))
print("First dictionary: ", d1)
print("Second dictionary: ", d2)
if len(d1) > len(d2):
    longDict = d1
    shortDict = d2
else:
    longDict = d2
    shortDict = d1
print("overlapping keys in the two dictionaries are:", end=' ')
for i in shortDict:
    if i in longDict:
        print(i, end=' ')
