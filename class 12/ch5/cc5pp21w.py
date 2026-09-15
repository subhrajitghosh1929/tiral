import csv
with open("example.csv", 'r', newline='') as file:
    reader = csv.reader(file, delimiter='\t')
    for row in reader:
        print(row)

