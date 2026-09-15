fileout=open("poem.txt","w")
#print("enter the line number ",i+1)
n=int(input("enter the number of time it will write :"))
for i in range(n):
    #print(name)
    #print("no. of bytes ",len(name))
    name=input(str("enter the poem"))
    fileout.write(f'{name}')
fileout.close()

