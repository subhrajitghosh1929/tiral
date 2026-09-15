stu={1:'Neha',2:'saima',3:'Avnit',4:'Ana',5:'Shaji'}
while len(stu)>=1:
    print("Element deleted :",stu.popitem())
    print(stu)
print("All element of dictionary got deleted in LIFO order ")
print(stu)

#2
print()
print("#2")
stu={1:'Neha',2:'saima',3:'Avnit',4:'Ana',5:'Shaji'}
print(stu.pop(4))
print("#1",stu)
print(stu.pop(6,"not here"))
print("#2",stu)
print(stu.pop(6,-1))
print("#3",stu)
print(stu.pop(6,None))
print("#4",stu) 
stu.clear()
print("#5",stu)
print("note the differene between the above and below")
stu={1:'Neha',2:'saima',3:'Avnit',4:'Ana',5:'Shaji'}
print("#6",stu.clear())
stu={1:'Neha',3:'saima',2:'Avnit',5:'Ana',4:'Shaji'}
print("#7",sorted(stu))
print("#8",sorted(stu,reverse=True))
print("#9",sorted(stu,reverse=False))
print("same as #7")
print("#10: sorting keys: ",sorted(stu.keys()))
print("#11: sorting values: ",sorted(stu.values()))
print("#12: sorting item: ",sorted(stu.items()))

"""del(stu)
print("#7",stu)"""

#3
print()
print("#3")
stu={1:'Neha',2:'saima',3:'Avnit',4:'Ana',5:'Shaji'}
key=3
x=stu.pop(key,None)
if x!=None:
    print('Removing pair is',(key,':',x,')'))

