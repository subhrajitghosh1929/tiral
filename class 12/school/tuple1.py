# Question
# Write a function to find the maximum and minimum values in a tuple.

def find_max_min(tup):
    max_value = max(tup)
    min_value = min(tup)
    return max_value, min_value
numbers = eval(input("enter the number in tuple form :"))
max_val, min_val = find_max_min(numbers)
print("Maximum Value:", max_val)
print("Minimum Value:", min_val)


