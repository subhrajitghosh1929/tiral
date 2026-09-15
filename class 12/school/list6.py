#Write a function to find the maximum sum of a contiguous sublist in a given list of integers.
def max_sublist_sum(lst):
    max_sum = float('-inf')
    current_sum = 0
    for num in lst:
        current_sum += num
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < 0:
            current_sum = 0
    return max_sum

input_list = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Maximum Sublist Sum:", max_sublist_sum(input_list))
