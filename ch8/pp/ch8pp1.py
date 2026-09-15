len = float(input("Enter length in cm: "))
if len < 0:
    print("Invalid input")
else:
    inch = len / 2.54
    print(len, "centimetres is equal to", inch, "inches")
