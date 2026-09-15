print("To print an empty tuple" ,tuple())
print("To print a tuple" ,tuple("abc"))
print("To print a tuple from a list: " ,tuple([1,2,3]))
print("To print a tuple from a dictionaty: " ,tuple({1:"1",2:"2",3:"3"}))
print("To print a list from a tuple of a list : " ,list[tuple([1,2,3])])  # list converted to tuple using tuple object
                                                                            # and back again to list using list object 
t1=eval(input("Enter a tuple: "))
lst=sorted(t1)
t1=tuple(lst)
print("Tuple after sorting:",t1)
