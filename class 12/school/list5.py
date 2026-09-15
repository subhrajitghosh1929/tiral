#Write a function to find the leaders in a list. An element is called a leader if there are no elements to its right that are greater than it.
def find_leaders(lst):
    leaders = []
    max_from_right = float('-inf')
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] > max_from_right:
            leaders.append(lst[i])
            max_from_right = lst[i]
    return leaders[::-1]

input_list = [16, 17, 4, 3, 5, 2]
print("Leaders in the List:", find_leaders(input_list))
