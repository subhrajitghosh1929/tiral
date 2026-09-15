# menu driven program 
radius=float(input("enter radius  of the circle :"))
print("1.calculate Area")       # menu1
print("2.calculate perimeter(circumference)")  # menu2
c=int (input("enter your choise(1 or 2):"))    # menu choice
if c==1:
    area=3.14159*radius*radius
    print("area of circle with radius",radius,'is',area)
elif c==2:
    perm=2*314159*radius
    print("circumference of circle with radius",radius,'is',perm)
else:
    print("Wrong choice entered")

