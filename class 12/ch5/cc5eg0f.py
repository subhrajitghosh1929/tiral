c=0
with open("poem.txt", 'r') as file:
    for line in file:
        c=c+1
        print(line.strip()+'\n')
print("the no. of lines",c)
