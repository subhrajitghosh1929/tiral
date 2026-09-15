# to find the longest word in a string(sentence)
str = input("Enter a string: ")
words = str.split()
longWord = ''
for w in words :
    if len(w) > len(longWord) :
        longWord = w
print("Longest Word =", longWord)
