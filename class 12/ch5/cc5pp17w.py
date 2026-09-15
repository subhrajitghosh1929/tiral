import pickle
def search_company(file_path, comp_id):
    try:
        # Open the file in binary read mode
        with open(file_path, 'rb') as file:
            # Deserialize the dictionary from the file
            company_data = pickle.load(file)
        
        # Search for the company with the specified CompID
        if comp_id in company_data:
            print(f"Company details for CompID {comp_id}:")
            print(company_data[comp_id])
        else:
            print(f"No company found with CompID {comp_id}.")
    
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example dictionary for COMPANY
COMPANY = {
    "1001": {"name": "Company A", "location": "City A", "industry": "IT"},
    "1002": {"name": "Company B", "location": "City B", "industry": "Finance"},
    "1003": {"name": "Company C", "location": "City C", "industry": "Healthcare"},
    "1004": {"name": "Company D", "location": "City D", "industry": "Engineering"},
    "1005": {"name": "Company E", "location": "City E", "industry": "Retail"}
}

# Specify the file path
file_path = 'COMPANY.DAT'
# Call the search function to search and display the company details for CompID '1005'
search_company(file_path, '1005')
