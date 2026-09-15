import struct
n=int(input("enter the number of books:- "))
# Function to create a new record and add it to Book.dat
def CreateFile(file_path):
    try:
        # Open the file in append binary mode
        with open(file_path, 'ab') as file:
            for i in range(n):
            # Input data for a new record (book)
                BookNo = int(input("Enter Book Number: "))
                Book_Name = input("Enter Book Name: ")
                Author = input("Enter Author Name: ")
                Price = float(input("Enter Price: "))
                # Pack the data into a binary format using struct.pack
                record = struct.pack('i 30s 30s f', BookNo, bytes(Book_Name, 'utf-8'), bytes(Author, 'utf-8'), Price)
            # Write the packed record to the file
            file.write(record)
        
        print(f"Record has been added to {file_path}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to count the number of books by a given author in Book.dat
def CountRec(file_path, author):
    try:
        count = 0
        # Open the file in read binary mode
        with open(file_path, 'rb') as file:
            # Calculate the size of each record (total 66 bytes based on the structure)
            record_size = struct.calcsize('i 30s 30s f')
            
            # Read the file until the end
            while True:
                record = file.read(record_size)
                if not record:
                    break
                
                # Unpack the record into individual fields
                unpacked_record = struct.unpack('i 30s 30s f', record)
                _, _, stored_author, _ = unpacked_record
                
                # Convert stored_author to string and strip null bytes
                stored_author = stored_author.decode('utf-8').strip('\x00')
                
                # Check if the stored_author matches the given author
                if stored_author == author:
                    count += 1
        
        print(f"Number of books by {author} in {file_path}: {count}")
        return count
    
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
file_path = 'Book.dat'

# (i) Create a new record and add it to Book.dat
CreateFile(file_path)

# (ii) Count the number of books by a given author (e.g., 'J.K. Rowling') in Book.dat
author_name = 'J.K. Rowling'  # Replace with the author name you want to count
CountRec(file_path, author_name)
