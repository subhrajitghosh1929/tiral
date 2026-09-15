# Question
# Write a function to calculate the average score from a dictionary of subject scores.
def calculate_average(scores):
    total = sum(scores.values())
    average = total / len(scores)
    return average

student_scores = {"Math": 85, "Science": 90, "English": 88, "History": 82}
avg_score = calculate_average(student_scores)
print("Average Score:", avg_score)

