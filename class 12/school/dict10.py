# Question
# How can you implement and manipulate nested dictionaries in Python? 
def add_to_nested_dict(nested_dict, keys, value):
    current = nested_dict
    for key in keys[:-1]:
        current = current.setdefault(key, {})
    current[keys[-1]] = value

grades = {}
add_to_nested_dict(grades, ["John", "Math"], 85)
add_to_nested_dict(grades, ["John", "Science"], 90)
add_to_nested_dict(grades, ["Alice", "Math"], 88)
print("Nested Dictionary:", grades)

