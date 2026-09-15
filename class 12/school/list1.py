#Write a function to count the number of even and odd numbers in a given list.
def count_even_odd(lst):
    even_count = sum( 1 for x in lst if x % 2 == 0)
    odd_count = len(lst) - even_count
    return even_count, odd_count
input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even, odd = count_even_odd(input_list)
print("Even Count:", even)
print("Odd Count:", odd)

