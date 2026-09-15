import pickle
stu ={}
# declare empty dictionary
found=False
fin=open('Stu. da' ,'rb' )
# open binary file
searchkeys = [12, 14]
#read from the file
try:
    print("Searching in File Stu.dat...")
    while True:
        stu = pickle.load(fin)
        if stu['Rollno'] in searchkeys:
            print(stu)
            found= True

except EOFError:
    if found == False:
        print("No such records found in the file")
    else:
        print("Search successful.")
    fin.close()

#close file
