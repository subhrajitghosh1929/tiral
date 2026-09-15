# Function to filter records
def filter_records(input_file, output_file):
    try:
        with open(input_file, 'r') as f_in:
            with open(output_file, 'w') as f_out:
                for line in f_in:
                    event, participant = line.strip().split(' - ')
                    if event == 'Athletics':
                        f_out.write(line + '\n')
        f_out.close()
        f_in.close()
    except FileNotFoundError:
        print(f"The file {input_file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Filter records to Athletics.dat
filter_records('sports.dat', 'Athletics.dat')

