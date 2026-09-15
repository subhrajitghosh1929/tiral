myfile=open(r'poem.txt',"r")
for i in range(5):
    str=myfile.read(30)
    print(str)
myfile.close()
