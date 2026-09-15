#Write a function to find the frequency of each element in a given list.
def frequency_of_elements(lst):
    frequency = {}
    for element in lst:
        if element in frequency:
            frequency[element] += 1
        else:
            frequency[element] = 1
    return frequency

input_list =eval(input("enter a list with some duplicate numbers :"))
print("Frequency of Elements:", frequency_of_elements(input_list))
