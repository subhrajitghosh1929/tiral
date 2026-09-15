
#ans 
# Function to read the file and display contents in two columns
"""def display_phonebook(filename):
    try:
        with open(telephone.txt, 'r') a2s file:
            print("*" * 30)
            for i in range(num):
                lines = file.readlines()
                print(lines)
                print("=" * 30)
                #print(f"{'s':<10} {'n'}")
        # Print the contents in two columns
        for line in lines:
            name, phone_number = line.split()
            print(f"{name:<10} {phone_number}")
    except FileNotFoundError:
        print(f"The file {telephone.txt} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
with open("telephone.txt", "r") as file:
    f = file.readlines()
    for line in f:
        name, number = line.split()
        print(name, '\t\t' ,number)"""
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

# Getting input from the user
file_name = input("Enter the name of the file containing telephone numbers ( file name : telephone.txt): ")
display_telephone_numbers(file_name)
  
#ans 
# Get the file path from the user
