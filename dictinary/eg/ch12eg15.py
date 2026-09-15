l=[]
n=int(input("how many students?"))
for a in range(n):
    r=int(input("enter a roll No. :"))
    l.append(r)
s=dict.fromkeys(l,2500)
print(s)
#s=dict.fromkeys(3)  it will give an error
#s=dict.fromkeys(3,)  it will give an error 
print("created dict.")
print(s)

"""
#2
print()
print("#2")
nd=dict.fromkeys([2,4,6,8],100)
print(nd)
nd1=dict.fromkeys((3,4,5))
print(nd1)
nd1=dict.fromkeys((3,4,5),(6,7,8))
print(nd1)
"""
