weight_in_kg=float(input("enter weight in Kg: "))
height_in_meter=float(input("enter height in meter: "))
bmi=weight_in_kg/(height_in_meter*height_in_meter)
print("BMI is :",bmi,end=" ")
if bmi <18.5:
    print("...under weight")
elif bmi<25:
    print("...normal")
elif bmi<30:
    print("...over weight")
else:
    print("...obese")
