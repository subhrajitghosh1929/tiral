temp = float(input("Enter Temperature in Celsius: "))
if temp < -273.15 :
    print("Temperature is invalid as it is below absolute zero")
elif temp == -273.15 :
    print("Temperature is absolute zero")
elif -273.15 <= temp < 0:
    print("Temperature is below freezing")
elif temp == 0 :
    print("Temperature is at the freezing point")
elif 0 < temp < 100:
    print("Temperature is in the normal range")
elif temp == 100 :
    print("Temperature is at the boiling point")
else :
    print("Temperature is above the boiling point")
