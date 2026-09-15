# to display a string without the vowels 
str = input("Enter a string: ").lower()
for ch in str : 
    if ch not in "aeiou":
        print(ch,end="")

