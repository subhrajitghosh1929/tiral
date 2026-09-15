#Write a function to interleave two lists of the same length.
def interleave_lists(lst1, lst2):
    return [item for pair in zip(lst1, lst2) for item in pair]
list1 =eval(input("enter a list of numbers :"))
list2 =eval(input("enter a list of numbers :"))
print("1st list is: ",list1)
print("2nd list is: ",list2)
print("Interleaved Lists:", interleave_lists(list1, list2))
