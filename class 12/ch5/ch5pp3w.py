fileout=open("telephone.txt","w")
s=str(input("enter the name :"))
n=int(input("enter the phone number :"))
fileout.write(f'{s},{n}\n')
fileout.close()
#ans 
# Function to read the file and display contents in two columns
def display_phonebook(telephone):
    try:
        with open(telephone.txt, 'r') as file:
            lines = file.readlines()
            
        # Print the headers
        print(f"{'Name':<10} {'Telephone Number'}")
        print("=" * 30)
        
        # Print the contents in two columns
        for line in lines:
            name, phone_number = line.split()
            print(f"{name:<10} {phone_number}")
    except FileNotFoundError:
        print(f"The file {telephone.txt} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
# Get the file path from the user

# Display the phonebook

