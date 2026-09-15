import random

def generate_random_number(num1, num2):
    low = min(num1, num2)
    high = max(num1, num2)
    return random.randint(low, high)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

for i in range(3):
    random_num = generate_random_number(num1, num2)
    print("Random number between", num1, "and", num2, ":", random_num)
