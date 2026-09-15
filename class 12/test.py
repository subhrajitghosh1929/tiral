import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",user="SUBH",password="#GODGAMERPR01#",database="SUBH")
if mycon.is_connected()==False:
    print("error connecting to mysql database")
cursor=mycon.cursor()
cursor.execute("select* from student")
data=cursor.fetchmany(3)
count=cursor.rowcount
for row in data:
    print(row)
mycon.close()
