import csv

def filter_csv(input_file, output_file):
    """
    Reads a CSV file and creates another CSV file with the same content
    except the lines beginning with 'check'.
    
    :param input_file: Path to the input CSV file.
    :param output_file: Path to the output CSV file.
    """
    try:
        with open(input_file, 'r', newline='') as f_in:
            reader = csv.reader(f_in)
            filtered_data = [row for row in reader ]#if not row[0].startswith('check')]
            print(filtered_data)
        with open(output_file, 'w', newline='') as f_out:
            writer = csv.writer(f_out)
            writer.writerows(filtered_data)
            print(writer.writerows(filtered_data))

        print(f"Filtered CSV file created successfully: {output_file}")
        
    except FileNotFoundError:
        print(f"The file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
filter_csv('input.csv', 'filtered.csv')
