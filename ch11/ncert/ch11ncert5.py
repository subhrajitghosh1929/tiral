tup=eval(input("enter tuple :"))
ln=len(tup)
lies =False
mn=min(tup)
if ln%2 == 0:
    half=ln//2
    if mn == tup[half] or mn == tup[half-1]:
        lies=True
else:
    half=ln//2
    if mn == tup[half]:
        lies = True
if lies == True:
    print("Minimum lies at tuple middle")
else:
    print("Minimum dosen't lie at tuple middle")
