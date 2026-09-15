
def display_lines_starting_with_k(filename):
    try:
        with open("MYNOTES.txt", 'r') as file:
            lines = file.readlines()
            for line in lines:
                if line.lstrip().startswith('k') or line.lstrip().startswith('k'):  # Use lstrip() to ignore leading whitespaces
                    print(line.strip())  # Use strip() to remove leading and trailing whitespaces
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
# Call the function with the filename MYNOTES.TXT
display_lines_starting_with_k('MYNOTES.TXT')
