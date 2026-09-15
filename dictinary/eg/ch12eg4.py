# initiallising of dictionary
e={}
e=dict()
e={"name":"Jhon","salary":10000,"age":24}
print(e["name"])
print(e["salary"])
print(e["age"])
print(e)
#creating dictionary using zip function 
e=dict(zip(("name","salary","age"),("Jhon",10000,24)))
print(e)
#creating dictionary using a list 
e=dict([["name","Jhon"],["salary",10000],["age",24]])
print(e)
#creating dictionary using a tuple
e=dict((["name","Jhon"],["salary",10000],["age",24]))
print(e)
#2
#using statement 
f={"name":"Jhon","salary":10000,"age":24}
del(f["name"])
print(f)
f={"name":"Jhon","salary":10000,"age":24}
del(f)

