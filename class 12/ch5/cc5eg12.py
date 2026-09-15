import pickle
stu = {}
file_path = 'Stu. dat'
try:
    with open(file_path, 'rb') as fin:
        print("File Stu.dat stores these records")
        while True:
            try:
                stu = pickle.load(fin)
                print(stu)
            except EOFError:
                break
            except pickle.UnpicklingError as e:
                print(f"Unpickling error: {e}")
                break
except FileNotFoundError:
    print(f"File {file_path} not found.")
except Exception as e:
    print(f"An error occurred: {e}")
