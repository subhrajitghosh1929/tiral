#1
print()
print("#1") 
while(3>4):             # 3<4 it will create infinite loop
    print("in loop")        
else:                   # 3>4 it will not execute the loop even once 
    print("exiting from while loop")

#2
print()
print("#2")
for a in range (10,1,-1):
    print("in loop",a)
else:                   # else works after normal termination of for loop
    print("exiting from for loop")
#3
print()
print("#3")
for i  in range (1,6):
    for j in range (1,i):
        print("*",end=" ")
    print()



#4
print()
print("#4")
for outer  in range (5,10,4):
    for inner in range (1,outer,2):
        print(outer, inner)


    
#5
print()
print("#5")
for a in range (3):
    for b in range (5,7):
        print("for a=",a,"b is now",b)
