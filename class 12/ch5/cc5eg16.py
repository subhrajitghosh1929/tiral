import pickle
stu ={}
found=False
print("Searching in file Stu.dat...")
with open('Stu.dat', 'rb') as fin:
    stu=p1ckle.load (fin)
    if stu['Marks'] > 81:
        print(stu)
        found = True
if found== False:
    print("No records with Marks > 81")
else:
    print("Search successful.")
