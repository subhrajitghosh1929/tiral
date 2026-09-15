def count_chars_until_dollar(file_path):
    try:
        # Open the file in read mode
        with open(file_path, 'r') as file:
            text = file.read()
        
        # Find the position of the first '$' symbol
        dollar_position = text.find('$')
        
        # If the '$' symbol is found, count the characters up to that point
        if (dollar_position != -1):
            print(f"Number of characters up to the first '$': {dollar_position}")
        else:
            # If no '$' symbol is found
            print("no '$' symbol is found")
            
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    # Call the count_chars_until_dollar function to read and count characters
count_chars_until_dollar('SAMPLE.TXT')
