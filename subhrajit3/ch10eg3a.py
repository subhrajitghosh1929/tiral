#1
print("#1")
lis=[13,18,11,16,18,14]
print(lis.index(18))
print(lis.append(33))     # may be asked as output
print(lis.index(33))
lst=lis    # a list can't be transfer to another list
lst=lis.append(12)
print(lst)

#2
print("#2")
t1=[1,3,5]
t2=[7,8]
t1.append(t2)
t1.append(10)
#t1.append(11,12)        # unable to append more than one item or element
t1.extend([11,12])   # in order to add more than one item than they must be enter as a list 
print (t1)          # use .extend([...])

#3
print("#3")
t1.insert(2,33)     # SYNTAX   .insert(index,item)
print (t1)
t1.pop(2)           # SYNTAX   .pop(index) to delete an item at index pos
print (t1)
t1.remove(11)       # SYNTAX   .remove(item) to delete an item 
print (t1)
print(t1.count(18))     # may be asked as output

t1.reverse()                # to reverse the entire list 
print (t1)          # may be asked as output (items in a list with in a list)


t2=['e','i','q','a','q','p']
print (t2)
t2.sort()          # may also be written as t2.sort(reverse=False)
print (t2)           # by default increasing order

t2.sort(reverse=True)
print(t2)
t2.sort(reverse=False)       # may be asked as output
print(t2)
print(max(t2))
print(min(t2))
t1=[1,3,5]
print(sum(t1))      # add up all integers 
'''sval=[17,24,15,30]
rsval.sorted(val,reverse=True)          # may also be written as t2.sort(reverse=False)
print (rsval) '''          # by default increasing order

t1.clear()          # to clear the whole list
print (t1)

#4
print("#4")
l2=[[1,2,3],[5,6]]      #it is known as ragged
print(l2)
