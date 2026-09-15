# Define a tuple of numbers
numbers_tuple = (221, 234, 657, 676, 190, 100)

# Create a list of unique elements
unique_elements = []
for num in numbers_tuple:
    if num not in unique_elements:
        unique_elements.append(num)

# Convert the list of unique elements to a tuple
unique_elements_tuple = tuple(unique_elements)

# Print the tuple of unique elements
print(unique_elements_tuple)

#2
print()
print("#2")
# Accept numbers in a tuple
numbers_input = input("Enter numbers separated by commas: ")
numbers_list = numbers_input.split(",")

# Convert input numbers to integers
numbers_tuple = tuple(int(num) for num in numbers_list)

# Print the elements with unique digits
unique_digits_list = [str(num) for num in numbers_tuple if len(str(num)) == len(str(num))]
print(",".join(unique_digits_list))
