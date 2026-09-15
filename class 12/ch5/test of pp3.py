# Writing to the file
fileout = open("telephone.txt", "w")
num = int(input("Enter the number of records (rows): "))
for i in range(num):
    name = input("Enter the name: ")
    phone_number = input("Enter the phone number: ")
    fileout.write(f'{name},{phone_number}\n')
fileout.close()
print("*"*25)
def display_telephone_numbers(file_name):
    try:
        with open(file_name, 'r') as file:
            print("{:<15}{}".format("Name", "Telephone Number"))
            print("-" * 30)
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 2:
                    name, number = parts
                    print("{:<15}{}".format(name, number))
                else:
                    print(f"Skipping invalid line: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    except Exception as e:
        print(f"Error reading file: {e}")

# Getting input from the user for the file name
file_name = input("Enter the name of the file containing telephone numbers: ")
display_telephone_numbers(file_name)

# Display the contents of the file
print("-----------------")
try:
    with open("telephone.txt", "r") as myfile:
        st = myfile.read()
        print(st)
except FileNotFoundError:
    print("Error: The file 'telephone.txt' was not found.")
