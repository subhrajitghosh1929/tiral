import pickle
stu={}
found=False
fin=open('Stu.dat','rb+')
try:
    while True:
        rpos= fin .tell()
        stu=pickle.load (fin)
        if stu['Rollno'] == 12:
            stu [' Name']=' Gurnam'
            fin.seek(rpos)
            pickle.dump (stu, fin)
            found=True
except EOFError:
    if found == False:
        print("Sorry, no matching record found.")
    else:
        print("Record(s) successfully updated.")
    fin.close()
