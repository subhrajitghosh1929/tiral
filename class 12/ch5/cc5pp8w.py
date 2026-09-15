# Function to append contents from source_file to destination_file
def append_file_contents(source_file, destination_file):
    try:
        with open(source_file, 'r') as f_source:
            with open(destination_file, 'a') as f_dest:
                for line in f_source:
                    f_dest.write(line)
        print(f"Contents of {source_file} have been appended to {destination_file}.")
    except FileNotFoundError:
        print(f"One of the files ({source_file} or {destination_file}) does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Get filenames from the user
source_file = input("Enter the name of the source file: ")
destination_file = input("Enter the name of the destination file: ")

# Append the contents of the source file to the destination file
append_file_contents(source_file, destination_file)


