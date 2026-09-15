def Show_words():
    """
    Reads the content of 'NOTES.TXT' and displays lines that contain exactly 5 words.
    """
    try:
        with open('NOTES.TXT', 'r') as file:
            lines = file.readlines()

            for line in lines:
                # Strip the line to remove leading/trailing whitespace and newline characters
                stripped_line = line.strip()
                print(stripped_line)
                # Split the line into words based on spaces
                words = stripped_line.split()
                print(words)
                # Check if the line contains exactly 5 words
                if len(words) == 5:
                    print(stripped_line)
    except FileNotFoundError:
        print("The file 'NOTES.TXT' does not exist.")
# Example usage to show lines with exactly 5 words
Show_words()
