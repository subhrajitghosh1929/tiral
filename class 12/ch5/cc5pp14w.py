def write_strings_to_file(file_path):
    try:
        # Open the file in write mode
        with open(file_path, 'w') as filout:
            while True:
                # Get the string from the user
                user_input = input("Enter a string to write to the file (or type 'exit' to quit): ")
                
                # Break the loop if the user types 'exit'
                if user_input.lower() == 'exit':
                    break
                # Write the string to the file
                filout.write(user_input + '\n')
        
        print(f"Strings have been written to {file_path}")
    
    except Exception as e:
        print(f"An error occurred: {e}")
write_strings_to_file('STRS.txt')
