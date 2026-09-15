# Question
# How can you implement a dictionary of dictionaries in Python?
def add_to_dict_of_dicts(dictionary, key1, key2, value):
    if key1 in dictionary:
        dictionary[key1][key2] = value
    else:
        dictionary[key1] = {key2: value}
grades = {}
add_to_dict_of_dicts(grades, "John", "Math", 85)
add_to_dict_of_dicts(grades, "John", "Science", 90)
add_to_dict_of_dicts(grades, "Alice", "Math", 88)
print("Dictionary of Dictionaries:", grades)

