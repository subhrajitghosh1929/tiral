import pickle
def search_staff(file_path, staff_code):
    try:
        # Open the file in binary read mode
        with open(file_path, 'rb') as file:
            # Deserialize the dictionary from the file
            staff_data = pickle.load(file)
        
        # Search for the staff code in the dictionary
        if staff_code in staff_data:
            print(f"Staff details for {staff_code}: {staff_data[staff_code]}")
        else:
            print(f"No staff found with the staff code {staff_code}.")
    
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example dictionary
Staff = {
    "S0101": {"name": "Alice Brown", "age": 34, "position": "Manager"},
    "S0102": {"name": "Bob Smith", "age": 28, "position": "Developer"},
    "S0103": {"name": "Charlie Johnson", "age": 45, "position": "Analyst"},
    "S0104": {"name": "Diana Green", "age": 31, "position": "Designer"},
    "S0105": {"name": "Edward White", "age": 40, "position": "Consultant"}
}

# Specify the file path
file_path = 'staff.dat'
# Call the search function to search and display the staff details for 'S0105'
search_staff(file_path, 'S0105')
