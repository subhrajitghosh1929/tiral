number={1:111,2:222,3:333,4:444}
print("Giving dictionary is : ",number)
max_key_values=max(number)
min_key_values=min(number)
print("Maximum and Minimum keys:",max_key_values,min_key_values)
max_values=max(number.values())
min_values=min(number.values())
print("Maximum and minimum value:",max_values,min_values)
key_sum=sum(number)
values_sum=sum(number.values())
print("Sum of dictionary's key: ",key_sum)
print("Sum of dictionary's value: ",values_sum)

#2
print()
print("#2")
d1={(1,2):'one',(3,4):'two'}
d2={'Green House':20,'Blue House':30,'Gray House':35}
d3={41:'N',12:'S',32:'A',24:'C'}
d4={1.5:'N',3.5:'S',3.2:'A',2.4:'C'}
print(min(d1),min(d2),min(d3),min(d4))
print(max(d1),max(d2),max(d3),max(d4))
#print(sum(d1))
print(sum(d3),sum(d4))
