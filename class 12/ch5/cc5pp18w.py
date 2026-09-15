import pickle
def search_trains_to_delhi(file_path):
    try:
        # Open the file in binary read mode
        with open(file_path, 'rb') as file:
            # Deserialize the list of dictionaries from the file
            train_data = pickle.load(file)
        
        # Initialize a list to store details of trains going to Delhi
        delhi_trains = []
        
        # Iterate through the list of dictionaries and find trains with destination "Delhi"
        for train in train_data:
            if train.get('destination') == 'Delhi':
                delhi_trains.append(train)
        
        # Display details of trains going to Delhi
        if delhi_trains:
            print(f"Details of trains going to Delhi:")
            for train in delhi_trains:
                print(train)
        else:
            print("No trains found with destination 'Delhi'.")
    
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example data for trains
trains = [
    {"train_id": "T001", "name": "Shatabdi Express", "destination": "Delhi", "departure_time": "08:00 AM"},
    {"train_id": "T002", "name": "Rajdhani Express", "destination": "Mumbai", "departure_time": "10:00 AM"},
    {"train_id": "T003", "name": "Duronto Express", "destination": "Delhi", "departure_time": "12:00 PM"},
    {"train_id": "T004", "name": "Garib Rath", "destination": "Kolkata", "departure_time": "02:00 PM"},
    {"train_id": "T005", "name": "Shatabdi Express", "destination": "Delhi", "departure_time": "04:00 PM"}
]

# Specify the file path
file_path = 'TRAIN.DAT'



# Search and display details of trains going to Delhi
search_trains_to_delhi(file_path)
