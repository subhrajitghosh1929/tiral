# Question
# Write a function to sort a dictionary by its values in Python. 

def sort_dict_by_value(input_dict):
    sorted_dict = {k: v for k, v in sorted(input_dict.items(), key=lambda item: item[1])}
    return sorted_dict

student_scores = {"Math": 85, "Science": 90, "English": 88, "History": 82}
sorted_scores = sort_dict_by_value(student_scores)
print("Sorted Dictionary by Value:", sorted_scores)

