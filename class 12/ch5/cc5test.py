file = open("myfile.txt","w")
L = ["This is Lagos \n","This is Python \n","This is Fcc \n"]
file.write("Hello There \n")
file.write(str(L))
file.writelines(L)
file.close()

