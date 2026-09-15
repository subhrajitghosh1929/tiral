def arcalc(x,y):
    return x+y,x-y,x*y,x/y,x%y
#_main_
num1=int(input("Enter a number 1:"))
num2=int(input("Enter a number 2:"))
add,sub,mult,div,mod=arcalc(num1,num2)
print("sum of given number :",add)
print("subtraction of given number :",sub)
print("Product of given number :",mult)
print("division of given number :",div)
print("Modulus of given number :",mod)
