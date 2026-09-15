import pickle
#declare empty dictionary object; it wi
emp ={}
empfile= open('Emp.dat', 'rb')
try:
    while True: 
        emp=pickle.load(empfile)
        print(emp)
except EOFError:
    empfile.close()
#close file
