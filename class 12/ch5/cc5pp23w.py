import csv

def convert_delimiter(input_file, output_file, new_delimiter):
  """
  Reads a CSV file and creates a new one with the same content
  but using a different delimiter.

  Args:
    input_file: Path to the input CSV file.
    output_file: Path to the output CSV file.
    new_delimiter: The new delimiter to use.
  """
  with open(input_file, 'r') as in_file, open(output_file, 'w') as out_file:
    reader = csv.reader(in_file)
    for row in reader:
      print(row)
      writer = csv.writer(out_file, delimiter=new_delimiter)
      writer.writerow(row)
    
# Example usage
convert_delimiter('original.csv', 'output.csv', ';')

def read_csv(file_name):
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
read_csv('output.csv')
