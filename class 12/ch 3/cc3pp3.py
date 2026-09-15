# Function to calculate cube of a number
def calculate_cube(number = 2):
    cube = number ** 3
    print("Cube of", number, "is", cube)

# Function to check if two characters are equal
def check_equal_chars(char1, char2):
    return char1 == char2

calculate_cube(3)
calculate_cube()

char1 = 'a'
char2 = 'b'
print("Characters are equal:", check_equal_chars(char1, char1))
print("Characters are equal:", check_equal_chars(char1, char2))
