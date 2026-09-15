import pickle

def write_staff_file(file_path, Staff):
    try:
        # Open the file in binary write mode
        with open(file_path, 'wb') as file:
            # Use pickle to serialize the dictionary and write it to the file
            pickle.dump(Staff, file)
        
        print(f"Dictionary has been written to {file_path}")
    
    except Exception as e:
        print(f"An error occurred: {e}")
Staff = {
    "S0101": {"name": "Alice Brown", "age": 34, "Member no.": "4567"},
    "S0102": {"name": "Bob Smith", "age": 28, "Member no.": "4571"},
    "S0103": {"name": "Charlie Johnson", "age": 45, "Member no.": "4579"},
    "S0104": {"name": "Diana Green", "age": 31, "Member no.": "4564"},
    "S0105": {"name": "Edward White", "age": 40, "Member no.": "4512"}
}

def search_staff(file_path):
    try:
        # Open the file in binary read mode
        with open(file_path, 'rb') as file:
            # Deserialize the dictionary from the file
            staff_data = pickle.load(file)
            print(staff_data)
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example dictionary


# Specify the file path
file_path = 'staff.dat'
