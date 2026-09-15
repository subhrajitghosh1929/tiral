# Question
# Write a function to group a list of tuples by their first element.

def group_by_first_element(tuples):
    groups = {}
    for tup in tuples:
        key = tup[0]
        if key in groups:
            groups[key].append(tup)
        else:
            groups[key] = [tup]
    return groups

tuples = [(1, 'a'), (2, 'b'), (1, 'c'), (3, 'd'), (2, 'e')]
grouped_result = group_by_first_element(tuples)
print("Grouped Tuples:", grouped_result)


