# to count the No. of words in a string(sentence) 
str = input("Enter a string: ")
count = 0
for ch in str :
    if ch.isspace() :
        count += 1
print("No of words =", count)
