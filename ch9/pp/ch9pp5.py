str = input("Enter the string: ")
sum = 0
digitStr = ''
for ch in str :
    if ch.isdigit() :
        digitStr += ch
        sum += int(ch)
if not digitStr :
    print(str, "has no digits")
else :
    print(str, "has the digits", digitStr, "which sum to", sum)
