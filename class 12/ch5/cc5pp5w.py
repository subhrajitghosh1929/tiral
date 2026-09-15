def AMCount(file_path):
    try:
        # Open the file in read mode
        with open(file_path, 'r') as file:
            text = file.read()
        
        # Initialize counters
        count_A = 0
        count_M = 0
        
        # Count occurrences of 'A', 'a', 'M', and 'm'
        for char in text:
            if char in 'Aa':
                count_A += 1
            elif char in 'Mm':
                count_M += 1
        
        # Display the counts
        print(f"Occurrences of 'A' and 'a': {count_A}")
        print(f"Occurrences of 'M' and 'm': {count_M}")
    
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
        
AMCount('STORY.txt')
