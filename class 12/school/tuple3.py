# Question
# Write a function to merge two tuples into a list of tuples using the `zip` function. 
def merge_tuples(tup1, tup2):
    merged_list = list(zip(tup1, tup2))
    return merged_list

tuple1 = eval(input("enter the number in tuple form :"))
tuple2 = eval(input("enter the number in tuple form :"))
merged_result = merge_tuples(tuple1, tuple2)
print(tuple1)
print(tuple2)
print("Merged List of Tuples:", merged_result)

