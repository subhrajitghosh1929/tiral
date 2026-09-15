fh=open("poem.txt","r")
fh.seek(15,2)
str1=fh.read(15)
print("Last 15 bytes of files contain: ",str1)
