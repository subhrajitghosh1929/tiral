name=""
while True :          #while True;    (boolean literal) creates an infinite loop  
    name=input("enter name('end' to exit):")
    if name == "end":       # to break the infinite looping 
        break
    print("Hello",name)
else:
    print("wasn't it fun ? ")

    
 #####2
print()
print("#2")
name=""
while name != "end": 
    name=input("enter name('end' to exit):")
    if name == "end":
        pass
    print("Hello",name)
else:
    print("wasn't it fun ? ")
   
#3
    print()
print("#3")
name=""
while 5 :          #while 5; creates an infinite loop for any non zero value   
    name=input("enter name('end' to exit):")
    if name == "end":       # to break the infinite looping 
        break
    print("Hello",name)
else:
    print("wasn't it fun ? ")
