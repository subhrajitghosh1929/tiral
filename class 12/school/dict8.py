# Question
# How can you implement a dictionary of lists in Python?
def add_to_dict_of_lists(dictionary, key, value):
    if key in dictionary:
        dictionary[key].append(value)
    else:
        dictionary[key] = [value]
scores = {}
add_to_dict_of_lists(scores, "Math", 85)
add_to_dict_of_lists(scores, "Math", 90)
add_to_dict_of_lists(scores, "Science", 88)
print("Dictionary of Lists:", scores)


