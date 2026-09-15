# Question
# Write a recursive function to flatten a nested tuple.

def flatten_tuple(nested_tup):
    flat_list = []
    for item in nested_tup:
        if isinstance(item, tuple):
            flat_list.extend(flatten_tuple(item))
        else:
            flat_list.append(item)
    return tuple(flat_list)

nested_tuple = (1, (2, 3), (4, (5, 6)))
flat_result = flatten_tuple(nested_tuple)
print("Flattened Tuple:", flat_result)

