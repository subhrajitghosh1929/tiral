str = input("Enter the string: ")
newStr = ""
for ch in str : 
    lch = ch.lower()
    if lch in 'aeiou':
        newStr += '*'
    else :
        newStr += ch
print(newStr)
