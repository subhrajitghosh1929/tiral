import pymysql as pym
mycon=pym.connect(host="localhost",user="SUBH",password="#GODGAMERPR01#",database="SUBH")
cursor=mycon.cursor()
cursor.execute("select* from student")
data=cursor.fetchmany(3)
for row in data:
    print(row)
mycon.close()
