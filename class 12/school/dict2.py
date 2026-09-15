# Question
# Write a function to merge two dictionaries and sum the values of common keys.

def merge_and_sum(dict1, dict2):
    merged_dict = {}
    for key in set(dict1) | set(dict2):
            merged_dict[key] = dict1.get(key, 0) + dict2.get(key, 0) 
    return merged_dict
dict1 = {"a": 100, "b": 200, "c": 300}
dict2 = {"b": 300, "d": 400}
merged_dict = merge_and_sum(dict1, dict2)
print("Merged and Summed Dictionary:", merged_dict)


