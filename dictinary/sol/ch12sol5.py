sen=input("Enter a sequence :")
sen.lower()
s=0
alphabatical_digits="abcdefghijklmnopqrstuvwxyz0123456789 "
char_count={}
print("Total character in sequence are:",len(sen))
for char in sen:
    if char in alphabatical_digits:
        s+=1
        if char in char_count:
            char_count[char]=char_count[char]+1
        else:
            char_count[char]=1
print(char_count)

#2
print("#2")
for x in char_count.items():
    print(x)
print("number of special char ",len(sen)-s)

s=0
lis=[]
lis=char_count.values()
for char in lis:
    s+=char
print("number of special char ",len(sen)-s)




