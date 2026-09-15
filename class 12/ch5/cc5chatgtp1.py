# Open a file in write mode
file_path = 'example.txt'

with open(file_path, 'w') as file:
    # Ask the user how many lines they want to write
    num_lines = int(input("How many lines do you want to write? "))

    # Loop to get user input and write to the file
    for i in range(num_lines):
        line = input(f"Enter text for line {i + 1}: ")
        file.write(f'{line}\n')

print('File created and text written successfully.')
