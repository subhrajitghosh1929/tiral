try:
    with open('Athletics.dat', 'r') as f_in:
        for line in f_in:
            print(line.strip().split(' - '))
            print(line)
except EOFError:
        f_in.close()
        f_out.close()
except FileNotFoundError:
    print("The file Athletics.dat does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")

