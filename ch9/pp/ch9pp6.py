str = input("Enter a few sentences: ")
length = len(str)
spaceCount = 0
alnumCount = 0

for ch in str :
    if ch.isspace() :
        spaceCount += 1
    elif ch.isalnum() :
        alnumCount += 1

alnumPercent = alnumCount / length * 100

print("Original Sentences:")
print(str)

print("Number of words =", (spaceCount + 1))
print("Number of characters =", (length))
print("Alphanumeric Percentage =", alnumPercent)
