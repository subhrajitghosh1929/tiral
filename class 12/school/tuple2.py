# Question
# Write a function to count the frequency of elements in a tuple.

def count_frequency(tup):
    frequency = {}
    for item in tup:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    return frequency

elements = eval(input("enter the number in tuple form :"))
frequency_dict = count_frequency(elements)
print("Element Frequency:", frequency_dict)

