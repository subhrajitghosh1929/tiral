str = input("Enter a string: ").lower()
count = 0
for ch in str : 
    if ch in "aeiou":
       count += 1
print("Vowel Count =", count)
