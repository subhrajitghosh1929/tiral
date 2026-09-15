with open(source_file, 'r') as f_in:
     for line in f_in:
        print(line.strip().split(' - '))
f_in.close()
