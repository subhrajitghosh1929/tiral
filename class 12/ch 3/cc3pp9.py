def generate_series(first, last):
    step = (last - first) // 3
    series = [first, first + step, first + 2 * step, last] 
    return series

first_value = int(input("Enter first value:"))
last_value = int(input("Enter last value:"))
result_series = generate_series(first_value, last_value)
print("Generated Series:", result_series)
