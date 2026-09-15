def calcsum(a,b,c):
    s=a+b+c
    return s
def average(x,y,z):
    sm=calcsum(x,y,z)
    return sm/3
num1=int(input("Num1..."))
num2=int(input("Num2..."))
num3=int(input("Num3..."))
print("Average of these number is",average(num1,num2,num3))
