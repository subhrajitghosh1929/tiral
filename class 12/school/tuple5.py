# Question
# Write a recursive function to calculate the sum of elements in a nested tuple.

def sum_nested_tuple(nested_tup):
    total = 0
    for item in nested_tup:
        if isinstance(item, tuple):
            total += sum_nested_tuple(item)
        else:
            total += item
    return total
nested_tuple = (1, (2, 3), (4, (5, 6)))
total_sum = sum_nested_tuple(nested_tuple)
print("Sum of Nested Tuple Elements:", total_sum)

