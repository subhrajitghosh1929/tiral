# Question
# Write a function to find the key with the maximum value in a dictionary of scores. 

def find_key_with_max_value(scores):
    max_key = max(scores, key=scores.get)
    return max_key

student_scores = {"Math": 85, "Science": 90, "English": 88, "History": 82}
key_with_max_value = find_key_with_max_value(student_scores)
print("Key with Maximum Value:", key_with_max_value)

