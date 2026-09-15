def min_ones_digit(num1, num2):
    ones_digit_num1 = num1 % 10
    ones_digit_num2 = num2 % 10
    if ones_digit_num1 < ones_digit_num2:
        return num1
    else:
        return num2

num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
result = min_ones_digit(num1, num2)
print("Number with minimum one's digit:", result)
