import mysql.connector as sqltor
connection=sqltor.connect(host="localhost",user="SUBH",password="#GODGAMERPR01#",database="SUBH")
cursor = connection.cursor()
st="select* from student where marks>%s and section='%s'"%(70,'B')
cursor.execute(st,(70,'B'))
data=cursor.fetchall()
for row in data :
    print(row)
cursor.close()
connection.close()
