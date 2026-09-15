line=input("Enter a line:")
lowercount=uppercount=0
digitcount=alphacount=symcount=0
for a in line :
    if a.islower():
        lowercount+=1
    elif a.isupper():
        uppercount+=1
    elif a.isdigit():
        digitcount+=1
    elif a.isalpha():       # error needs to be checked
        alphacountt+=1
    elif a.isalnum()!= True and a != ' ':        # for counting specila character 
        symcount+=1
    elif a.isalnum() == False and a != ' ':        # for counting specila character 
        symcount+=1
print("Number of uppercase letters: ",uppercount)
print("Number of lowercase letters: ",lowercount)
print("Number of alphabets: ",alphacount)
print("Number of digit: ",digitcount)
print("Number of symbol: ",symcount)
print("Number of symbol: ",symcount)  
