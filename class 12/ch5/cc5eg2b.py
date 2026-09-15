myfile=open('poem.txt',"r")
for i in range(5):
    s=myfile.readlines()
    linecount=len(s)
    print("number of lines in poem.txt is",linecount+1)
myfile.close()
