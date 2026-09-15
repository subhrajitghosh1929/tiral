
with open("Article.txt", 'r') as file:
    text = file.read()
    count = 0
    for char in text:
        if char.isupper():
            count += 1
print("number of uppercase character present in : ",text," are : ", count)

