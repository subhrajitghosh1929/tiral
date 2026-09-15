myfile=open("poem.txt","r")
str1=""
size=0
tsize=0
while str1:
    str=myfile.readlines()
    tsize=tsize+len(str1)
    size= size+len(str1.strip())
print("size of file after removing all EOL character & blank line :",size)
print("The total size of the file: ",tsize)
myfile.close()
