#Write a function to find the median of a given list.
def find_median(lst):
    sorted_list = sorted(lst)
    length = len(sorted_list)
    mid = length // 2
    if length % 2 == 0:
        return (sorted_list[mid - 1] + sorted_list[mid]) / 2
    else:
        return sorted_list[mid]
input_list = eval(input("enter a list of numbers :"))
print("Median of List:", find_median(input_list))
