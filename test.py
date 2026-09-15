ans=True
while ans:
    keys=eval(input("enter the keys :"))
    values=eval(input("enter the values :"))
    numbers=dict(zip(keys,values))
    print("given two list :",keys,values)
    print("dict created ",numbers)
    n=eval(input("Enter the index position of the key to be changed : "))
    m=eval(input("Enter the value of the key to be changed : "))
    lk=list(numbers.keys())
    lk[n]=m
    print("the new dict is ",dict(zip(lk,values)))
    ans=input("to continue write True ,to exit write False :")
