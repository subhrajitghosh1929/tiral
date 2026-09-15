ht = int(input("Enter your height in centimeters: "))
htInInch = ht / 2.54;
feet = htInInch // 12;
inch = htInInch % 12;
print("Your height is", feet, "feet and", inch, "inches")
