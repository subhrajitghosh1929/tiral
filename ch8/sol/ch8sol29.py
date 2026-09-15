import random
n=int(input("how many dice throws ?"))
for i in range(1,n+1):
    print("throw",i,":",random.randint(1,6))
