sale=int(input("enter the amount of monthly sell: "))
if sale>=30000:
    discount=sale*0.18
elif sale>=20000:
    discount=sale*0.15
elif sale>=10000:
    discount=sale*0.10
else:
    discount=sale*0.05
print("discount sale:",discount)

