new_dict={}
for i in range(10):
    new_dict.setdefault(i)
print("Dictinary is")
print(new_dict)

#2
print()
print("#2")
emp1={'name':"Jhon",'salary':10000,'age':24}
emp2={'name':"Diya",'salary':54000,'dept':'Sale'}
print("dict 1 : ",emp1)
print("dict 2 : ",emp2)
emp1.update(emp2)
print(emp1)
# almost same as update()
print("# almost same as update()")
for k in emp1.keys():
    emp2[k]=emp1[k]
print(emp2)    
# note the difference between update above program snippet
print("# note the difference between update above program snippet ")

#3
print()
print("#3")
emp2={'name':"Diya",'salary':54000,'dept':'Sale'}
emp=emp2.copy()
print(emp)
#same as copy()
print("#same as copy()")
emp3=emp2
print(emp3)
emp3['age']=24
print(emp3)

#4
print()
print("#4")
d1={1:[1,2,3],2:[3,4,5]}
d2=d1
print(d2)
d2[1].append(4)
print(d1)
#same as copy()
print("#same as copy()")
d2=d1.copy()
print(d2)
d2[1].append(4)
print(d1)

#5
print()
print("#5")
old={'name':'vini','age':25}
new=old.copy()
new['name']='Tony'
print(old)
print(new)

#6
print()
print("#6")
old={'name':['vini','rini'],'age':[25,23]}
new=old.copy()
new['name'].append('Tony')
print(old)
print(new)
