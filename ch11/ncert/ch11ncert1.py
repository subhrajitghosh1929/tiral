T=(23,45,34,66,77,67,70)
maxvalue=max(T)
length=len(T)
secmax=0
for a in range(length):
    if secmax < T[a] < maxvalue:
        secmax=T[a]
print("second Largest value is:",secmax)


