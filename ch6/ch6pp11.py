p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = int(input("Enter time: "))
si = (p * r * t) / 100
ci = p * ((1 + (r / 100 ))** t) - p
print("Simple interest = ", si)
print("Compound interest = ", ci)
print("The amount of interest earned more by ci ",ci-si)
