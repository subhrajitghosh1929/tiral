# Open the file in read mode ('r')
with open("Answer.txt", "r") as myfile:
    line = myfile.readline()  # Read the first line
    while line:
        # Print each word in the line using split()
        for word in line.split():
            print(word,end='#')
        print()
        line = myfile.readline()  # Read the next line
