tup=eval(input("enter input for tuple: "))
t=tup[3:-3]
t0=tup[3:tup[5]]
t1=tup[::-3]
t2=tup[2:8:2]
t3=tup[3:30]
print("two created tuple are:")
print("Tuple:",t)
print("Tuple0:",t0)
print("Tuple1:",t1)
print("Tuple2:",t2)

print("Tuple3:",t3)
print(tup[2:5]*3)
print(tup[2:5]+(3,4))
