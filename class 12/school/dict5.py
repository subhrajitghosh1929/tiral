# Question
# Write a function to generate a dictionary of Fibonacci numbers up to a given limit.
def generate_fibonacci_dict(n):
    fibonacci_dict = {}
    a, b = 0, 1
    for i in range(n):
        fibonacci_dict[i+1] = a
        a, b = b, a + b
    return fibonacci_dict

n = 10
fibonacci_dict = generate_fibonacci_dict(n)
print("Fibonacci Dictionary:", fibonacci_dict)

