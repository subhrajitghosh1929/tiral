# to check equality of opening and closing () in a formula
str = input("Enter a formula: ")
count = 0
for ch in str :
    if ch == '(' :
        count += 1
    elif ch == ')' :
        count -= 1
if count == 0 :
    print("Formula has same number of opening and closing parentheses")
else :
    print("Formula has unequal number of opening and closing parentheses")


# rectifi the Error 
