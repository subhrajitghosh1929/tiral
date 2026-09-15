def count_lines_starting_with_a(filename):
    try:
        count = 0
        with open(filename, 'r') as file:
            for line in file:
                if line.strip().startswith('A')or line.strip().startswith('a'):
                    print(line.strip())
                    count += 1
        print(f"Number of lines starting with 'A' in {filename}: {count}")
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
count_lines_starting_with_a('LINES.txt')
