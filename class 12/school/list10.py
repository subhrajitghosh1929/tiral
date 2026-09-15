#Write a function to rotate a given list to the right by a specified number of positions.
def rotate_right(lst, n):
    n = n % len(lst)
    return lst[-n:] + lst[:-n]
input_list = eval(input("enter a list of numbers :"))
positions = int(input("enter the number of position you want to rotate by :"))
print("List Rotated to the Right:", rotate_right(input_list, positions))
