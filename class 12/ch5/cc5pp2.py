def filter_records(input_file, output_file):
    with open(input_file, 'r') as f_in:
        with open(output_file, 'w') as f_out:
            for line in f_in:
                event, participant = line.strip().split(' - ')
                if event == 'Athletics':
                    f_out.write(line)
filter_records('sports.dat', 'Athletic.dat')
