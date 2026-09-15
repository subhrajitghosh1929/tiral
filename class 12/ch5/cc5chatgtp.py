# Open a file in write mode
with open('example.txt', 'w') as file:
    # Loop to write multiple lines to the file
    for i in range(1, 11):  # Writing 10 lines as an example
        file.write(f'This is line {i}\n')
print('File created and text written successfully.')
