import mysql.connector as sqlcon
con=sqlcon.connect(host="localhost",user="root",passwd="12345",database='',auth_plugin="mysql_native_password")
cursor=con.cursor()
