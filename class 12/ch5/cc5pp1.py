with open("input.txt", 'r') as f:
    with open("output.txt", 'w') as fout:
        for line in f:
            modified_line = ' '.join(line.split())
            fout.write(modified_line + '\n')
