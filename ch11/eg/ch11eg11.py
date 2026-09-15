tup=eval(input("enter input for tuple: "))
t1=tup[2:8:2]
t2=tup[-3:-9:-2]
t3=t2[::-1]
if t3==t1:
    print("the two tuple contain the same element in reverse order.")
else:
    print("the two tuple contain different element.")
