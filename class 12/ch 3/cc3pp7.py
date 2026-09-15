import random
def generate_number(n):
    lower_bound = 10 ** (n - 1)  
    upper_bound = (10 ** n) - 1   
    return random.randint(lower_bound, upper_bound)

n = int(input("Enter the value of n:"))
random_number = generate_number(n)
print("Random number:", random_number)
