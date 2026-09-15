# Question
# Write a function to calculate the product of all elements in a tuple.

def product_of_elements(tup):
    product = 1
    for item in tup:
        product *= item
    return product

numbers = eval(input("Enter the elements of tuple: "))
product_result = product_of_elements(numbers)
print("Product of Tuple Elements:", product_result)

