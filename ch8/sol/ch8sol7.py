import math
num=int(input("Enter number: "))
ln= len(str(num))
lst=num%10
fst=num// math.pow(10,ln-1)
print("length of given number",num,"is",ln)
print("The first digit is",fst)
print("The last digit is",lst)
print("first digit rising to the length:",\
math.pow(fst,ln))
print("last digit rising to the length:",\
math.pow(lst,ln))
