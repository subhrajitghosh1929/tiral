# Question
# Write a function to find common elements between two tuples using set operations.

def find_common_elements(tup1, tup2):
    common_elements = set(tup1) & set(tup2)
    return common_elements

tuple1 = eval(input("Enter the elemets of 1st tuple:"))
tuple2 = eval(input("Enter the elemets of 2st tuple:"))
common_result = find_common_elements(tuple1, tuple2)
print("Common Elements:", common_result)
