T=(23,45,34,66,77,67,70)
maxvalue=max(T)
length=len(T)
secmax=0
thmax=0
for a in range(length):
    if secmax < T[a] < maxvalue:
        secmax=T[a]
for a in range(length):
    if  thmax < T[a] < secmax :
        thmax=T[a]
print("Largest value is:",maxvalue)
print("second Largest value is:",secmax)
print("third Largest value is:",thmax)

