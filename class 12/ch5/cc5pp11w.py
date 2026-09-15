def read_and_categorize_characters():
    try:
        with open('LOWER.txt', 'w') as lower_file, \
             open('UPPER.txt', 'w') as upper_file, \
             open('OTHERS.txt', 'w') as others_file:
            print("Enter characters one by one. Enter 'STOP' to stop the input.")
            while True:
                char = input("Enter a character: ")

                if char == "STOP":
                    break
                
                if char.islower():
                    lower_file.write(char + '\n')
                elif char.isupper():
                    upper_file.write(char + '\n')
                else:
                    others_file.write(char + '\n')
                    
    except Exception as e:
        print(f"An error occurred: {e}")
    lower_file.close()
    upper_file.close()
    others_file.close()
    print("Characters have been categorized and written to files.")
   
read_and_categorize_characters()



