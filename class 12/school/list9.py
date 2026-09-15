#Write a function to find the Kth largest element in a given list.
def kth_largest(lst, k):
    sorted_list = sorted(lst, reverse=True)
    return sorted_list[k - 1] if k <= len(sorted_list) else None
input_list = eval(input("enter a list of numbers :"))
k =int(input("enter the value of K for Kth largest element :"))
print("Kth Largest Element:", kth_largest(input_list, k))
