# type c data handaling
#pg-220
#23
p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))
si = p * r * t / 100
amt = p + si
print("Amount Payable =", amt)
