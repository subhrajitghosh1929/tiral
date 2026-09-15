#Read
#1
"""with open("output.txt", 'r') as ft:
        for line in ft:
            print(line)
#2
try:
    with open('Athletics.dat', 'r') as f_in:
        for line in f_in:
            print(line.strip().split(' - '))
except EOFError:
        f_in.close()
        f_out.close()
except FileNotFoundError:
    print("The file Athletics.dat does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
f_in.close()
#3
# Display the phonebook
myfile=open(r'telephone.txt',"r")
st=myfile.read()
print(st)
#4

#5

#6
with open('Article.txt', 'r') as f_in:
     for line in f_in:
        print(line.strip().split(' - '))
f_in.close()
#7

#8
# Display the contents of the source file
destination_file = input("Enter the name of the destination file: ")
with open(destination_file, 'r') as fl_out:
    for line in fl_out:
        print(line.strip())
#9
with open("MYNOTES.txt", 'r') as fl_out:
    for line in fl_out:
        print(line.strip())
#10

#11
#
def read_file(file_name):
    try:
        with open(file_name, "r") as file:
            contents = file.read()
            print(f"Contents of {file_name}:")
            #print(contents)
            print(contents if contents else "(empty)")
    except FileNotFoundError:
        print(f"{file_name} not found. Please make sure the file exists.")


read_file("LOWER.txt")
read_file("UPPER.txt")
read_file("OTHERS.txt")

#12

#13

#14
with open("STRS.txt", 'r') as fl_out:
    for line in fl_out:
        print(line.strip())
#15
with open("member.dat", 'rb') as fl_out:
    for line in fl_out:
        print(line)"""
#20
with open("NOTES.txt", 'r') as file:
    for line in file:
        print(line.strip()+'\n')   
        
        


