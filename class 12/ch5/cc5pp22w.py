import csv
def write_nested_list(data, file_name):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    
def read_csv(file_name):
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

nested_list = [['Name', 'Age', 'Gender'],
                ['Prateek', '14', 'Male'],
                ['Ananya', '24', 'Female'],
                ['Aryan', '44', 'Male']]


write_nested_list(nested_list, 'output.csv')

print("Content of 'output.csv':")
read_csv('output.csv')
