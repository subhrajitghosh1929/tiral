# Question
# Write a function to rotate the elements of a tuple by k positions.

def rotate_tuple(tup, k):
    k = k % len(tup)  # To handle cases where k > len(tup)
    return tup[-k:] + tup[:-k]

numbers = eval(input("Enter the elements of tuple"))
k = int(input("enter the k position :"))
rotated_tuple = rotate_tuple(numbers, k)
print("Rotated Tuple:", rotated_tuple)

