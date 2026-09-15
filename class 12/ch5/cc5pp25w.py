import csv
n=int(input("enter the number of records:- "))
def add():
    with open('furdata.csv', mode='w', newline='') as file:
        for i in range (n):
            writer = csv.writer(file)
            fid = input("Enter furniture id: ")
            fname = input("Enter furniture name: ")
            fprice = float(input("Enter furniture price: "))
            writer.writerow([fid, fname, fprice])
        print("Record added successfully to 'furdata.csv'")
    
def search():
    found = False
    with open('furdata.csv', mode='r') as file:
        reader = csv.reader(file)
        print("Records of furniture with price more than 10000:")
        for row in reader:
            if len(row) == 3 and float(row[2]) > 10000:
                print("Furniture ID:", row[0])
                print("Furniture Name:", row[1])
                print("Furniture Price:", row[2])
                print()
                found = True
    
    if found == False:
        print("No records of furniture with price more than 10000 found")

add()
search()
