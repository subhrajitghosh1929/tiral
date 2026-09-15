print("part A")
lis=[]
for i in range (50):
    lis.append(i)
print(lis)

print("part B")
lis1=[]    
for i in range (1,51):
    lis1.append(i*i)
print(lis1)
    
print("part C")
pattern=""
lis2=[]
for a in range(97,123):      # printing pattern using ASCII value
    pattern=(chr(a))*(a-96)
    lis2.append(pattern)
print(lis2)
