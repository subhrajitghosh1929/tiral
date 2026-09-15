fileinp=open(r'Marks.txt',"r")
#while str:
for i in range(2):
    str=fileinp.read()
    print(str)
fileinp.close()
