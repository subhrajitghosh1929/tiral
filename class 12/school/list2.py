#Write a function to rotate a list to the left by a given number of positions.
def rotate_left(lst, n):
    n = n % len(lst)
    return lst[n:] + lst[:n]
input_list = eval(input("enter a list of numbers :"))
positions = int(input("enter the number of positions to shifted : "))
print("The origial list is: ",input_list)
print("List Rotated to the Left by ",positions," is :", rotate_left(input_list, positions))
