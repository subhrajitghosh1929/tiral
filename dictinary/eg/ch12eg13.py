#1
print()
print("#1")
text="this is sample string"
word=text.split()
print(word)
print("length of text is",len(text))

#2
print()
print("#2")
emp1={'salary':10000,'dept':'Sale','age':24,'name':"Jhon"}
print("the dictionary is",emp1)
print(emp1.get('dept'))
print(emp1.get('desig'))
print(emp1.get('desig',"not yet"))
print("the items(keys) of the dictionary are",emp1.items())
print("the keys of the dictionary are")
for x in emp1:
    print(x)

print("the keys:values of the dictionary are")
for x,y in emp1.items():
    print(x,y)
    
print("the keys of the dictionary are",emp1.keys())
print("the values of the dictionary are",emp1.values())
