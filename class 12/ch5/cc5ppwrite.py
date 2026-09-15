#1
fileout=open("input.txt","w")
n=int(input("enter the number of time it will write : "))
for i in range(n):
    name=input(str("enter the poem : "))
    fileout.write(f'{name}\n')
fileout.close()
"""#2
fileout = open("sports.dat", "w")
n = int(input("Enter the number of records to write: "))
for i in range(n):
    name = input("Event - Participant: ")
    fileout.write(f'{name}\n')
fileout.close()
#3
fileout=open("telephone.txt","w")
num=int(input("enter the number of records(rows): "))
for i in range(num):
    s=input("enter the name :")
    n=input("enter the phone number : ")
    fileout.write(f'{s},{n}\n')
fileout.close()
#4
fileout=open("poem.txt","w")
#print("enter the line number ",i+1)
n=int(input("enter the number of time it will write :"))
for i in range(n):
    #print(name)
    #print("no. of bytes ",len(name))
    name=input(str("enter the poem"))
    fileout.write(f'{name}\n')
fileout.close()
#5
# Content to write to STORY.TXT
n=int(input("enter the number of time it will write :"))
with open("STORY.txt", 'w') as file:
    for i in range(n):
          s=input("enter the poem :")
          file.write(s)
#6
fileout=open("Article.txt","w")
n=str(input("enter the lines:"))
fileout.write(f'{n}\n')
fileout.close()
#7
source_file = input("Enter the name of the source file: ")
fileout=open(source_file,"w")
n=str(input("enter the lines:"))
fileout.write(f'{n}\n')
fileout.close()
#8
# Get the name of the source file and write to it
source_file = input("Enter the name of the source file: ")

with open(source_file, "w") as fileout:
    n = int(input("Enter the number of lines to write: "))
    for i in range(n):
        line = input(f"Enter line {i + 1}: ")
        fileout.write(f'{line}\n')
#9
with open("MYNOTES.txt", "w") as fileout:
    n = int(input("Enter the number of lines to write: "))
    for i in range(n):
        line = input(f"Enter line {i + 1}: ")
        fileout.write(f'{line}\n')
#10

#11
        
#12
with open("LINES.txt", "w") as fileout:
    n = int(input("Enter the number of lines to write: "))
    for i in range(n):
        line = input(f"Enter line {i + 1}: ")
        fileout.write(f'{line}\n')
#13
# Write the content to SAMPLE.TXT in write mode
with open('SAMPLE.TXT', 'w') as file:
    n = int(input("Enter the number of lines to write: "))
    s=str(input("enter the lines:"))
    file.write(s)
#16
import pickle

def write_staff_file(file_path, data):
    try:
        # Open the file in binary write mode
        with open(file_path, 'wb') as file:
            # Use pickle to serialize the dictionary and write it to the file
            pickle.dump(data, file)
        
        print(f"Dictionary has been written to {file_path}")
    
    except Exception as e:
        print(f"An error occurred: {e}")
Staff = {
    "S0101": {"name": "Alice Brown", "age": 34, "position": "Manager"},
    "S0102": {"name": "Bob Smith", "age": 28, "position": "Developer"},
    "S0103": {"name": "Charlie Johnson", "age": 45, "position": "Analyst"},
    "S0104": {"name": "Diana Green", "age": 31, "position": "Designer"},
    "S0105": {"name": "Edward White", "age": 40, "position": "Consultant"}
}
file_path = 'staff.dat'
write_staff_file(file_path, Staff)
#17
import pickle
def write_company_file(file_path, data):
    try:
        # Open the file in binary write mode
        with open(file_path, 'wb') as file:
            # Use pickle to serialize the dictionary and write it to the file
            pickle.dump(data, file)
        
        print(f"Dictionary has been written to {file_path}")
    
    except Exception as e:
        print(f"An error occurred: {e}")
COMPANY = {
    "1001": {"name": "Company A", "location": "City A", "industry": "IT"},
    "1002": {"name": "Company B", "location": "City B", "industry": "Finance"},
    "1003": {"name": "Company C", "location": "City C", "industry": "Healthcare"},
    "1004": {"name": "Company D", "location": "City D", "industry": "Engineering"},
    "1005": {"name": "Company E", "location": "City E", "industry": "Retail"}
}
file_path = 'COMPANY.DAT'
# Write the COMPANY dictionary to the pickled file
write_company_file(file_path, COMPANY)
#18
import pickle
def write_train_file(file_path, data):
    try:
        # Open the file in binary write mode
        with open(file_path, 'wb') as file:
            # Use pickle to serialize the list of dictionaries and write it to the file
            pickle.dump(data, file)
        
        print(f"Data has been written to {file_path}")
    
    except Exception as e:
        print(f"An error occurred: {e}")
trains = [
    {"train_id": "T001", "name": "Shatabdi Express", "destination": "Delhi", "departure_time": "08:00 AM"},
    {"train_id": "T002", "name": "Rajdhani Express", "destination": "Mumbai", "departure_time": "10:00 AM"},
    {"train_id": "T003", "name": "Duronto Express", "destination": "Delhi", "departure_time": "12:00 PM"},
    {"train_id": "T004", "name": "Garib Rath", "destination": "Kolkata", "departure_time": "02:00 PM"},
    {"train_id": "T005", "name": "Shatabdi Express", "destination": "Delhi", "departure_time": "04:00 PM"}
]
file_path = 'input.dat'
# Write example data to TRAIN.DAT
write_train_file(file_path, trains)
#20
def write_notes_file():
   
    Writes sample content to 'NOTES.TXT'.
    
    content = The file contains many sentences.
This is a sample file.
But need only sentences which have only 5 words.
Another line with five words here.

    # Open the file in write mode and write the content to it
    with open('NOTES.TXT', 'w') as file:
        file.write(content)
# Write the content to the file
write_notes_file()
#21
import csv
def write_example_csv(output_file):
    # Sample data to write to the CSV
    data = [
        ['Name', 'Age', 'City'],
        ['Alice', '30', 'New York'],
        ['Bob', '25', 'Los Angeles'],
        ['Charlie', '35', 'Chicago']
    ]
    # Write the CSV data to a file using 'w' mode
    with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile, delimiter='\t')
        for row in data:
            writer.writerow(row)

# Example usage
output_file = 'example.csv'  # The output file name
write_example_csv(output_file)

print(f"Data has been written to {output_file}.")

#23
import csv
def write_example_csv(output_file):
    # Sample data to write to the CSV
    data=Reads a CSV file with a given delimiter and overwrites it with the same content using a different delimiter.

    :param file_path: The path to the CSV file.
    :param input_delimiter: The delimiter used in the input CSV file (default is ',').
    :param output_delimiter: The delimiter to be used in the output CSV file (default is ';').
    
    # Write the CSV data to a file using 'w' mode
    with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile, delimiter='\t')
        for row in data:
            writer.writerow(row)

# Example usage
output_file = 'original.csv'  # The output file name
write_example_csv(output_file)

print(f"Data has been written to {output_file}.")
#24
import csv

def create_sample_csv(filename):
    # Define sample data for the CSV file
    data = [
        ["checkitem1", "value1", "value2"],
        ["row2", "data1", "data2"],
        ["checkitem2", "value3", "value4"],
        ["row4", "data3", "data4"],
        ["checkitem3", "value5", "value6"],
        ["row6", "data5", "data6"],
    ]

    # Write data to a CSV file
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)
    
    print(f"Sample CSV file '{filename}' created successfully.")

# Create the sample input.csv file
create_sample_csv('input.csv')"""

















      
