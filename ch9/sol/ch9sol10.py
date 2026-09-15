s=input("enter a line of text:")
count=0
for word in s.split():
    print(word)
    count+=1
print("Total word:",count)
