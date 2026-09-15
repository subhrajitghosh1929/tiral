# Question
# Write a function to replace all occurrences of an element in a tuple.

def replace_element(tup, old, new):
    return tuple(new if x == old else x for x in tup)

numbers = eval(input("enter the elements in tuple :"))
old_value = eval(input("enter the element to be replaced :"))
new_value = eval(input("enter the new element to be replaced with :"))
replaced_tuple = replace_element(numbers, old_value, new_value)
print("Replaced Tuple:", replaced_tuple)

