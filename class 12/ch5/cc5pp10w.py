
def DISPLAYWORDS(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                words = line.split()
                for word in words:
                    if len(word) < 4:
                        print(word)
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Create STORY.TXT with some sample lines for testing
def create_story_file(filename):
    lines = [
        "This is a story about a cat.",
        "The cat is very cute and small.",
        "It likes to play and run around."
    ]
    try:
        with open(filename, 'w') as file:
            for line in lines:
                file.write(line + '\n')
        print(f"{filename} has been created with sample lines.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Create STORY.TXT with sample lines
create_story_file('STORY.TXT')

# Display words from STORY.TXT that are less than 4 characters long
DISPLAYWORDS('STORY.TXT')
