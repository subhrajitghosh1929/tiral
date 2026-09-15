myfile = open("Answer.txt", 'r')
ch = myfile.read(1)  # Read the first character
vcount = 0
ccount = 0

while ch:  # Loop until the end of the file
    if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
        vcount += 1
    elif ch.isalpha():
        ccount += 1
    ch = myfile.read(1)  # Read the next character

print("Vowels in the file:", vcount)
print("Consonants in the file:", ccount)
myfile.close()
