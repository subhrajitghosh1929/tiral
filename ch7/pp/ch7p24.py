# type c data handaling
#pg-220
#24
p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))
amt = p * (1 + r / 100) ** t
print("Amount Payable =", amt)
