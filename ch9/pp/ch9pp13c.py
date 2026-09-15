str = input("Enter a string: ").lower()
for ch in str : 
    if ch in "aeiou":
       print(ch.upper(),end="")
    else:
        print(ch,end="")


