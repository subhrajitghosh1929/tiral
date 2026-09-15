d=int(input("Enter deposit: "))
t=int(input("Enter time: "))
    # NAMING OF CONDITIONS
ef5p= d<2000 and t>=2
    # when deposit is less than Rs. 2000 and for 2 years or more at 5%/a
ef7p= 2000>=d <=6000 and t>=2
    # when deposit is Rs. 2000 or more than but less than equal to 6000 and for 2 years or more at 7%/a
ef8p= d>= 6000 and t>=1
    # when deposit is more than Rs. 6000 and for 1 years or more at 8%/a
ef10p= t>=5
    # when all deposit for 5 years or more at 10%/a
if ef5p:        # means ef5p == True
    r=5
elif ef7p:        # means ef7p == True
    r=7
elif ef8p:        # means ef8p == True
    r=8
elif ef10p:        # means ef10p == True
    r=10
else:
    r=0
si=d*t*r/100
print("si = ",si)

