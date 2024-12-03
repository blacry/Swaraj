import Room_Boking
import correction
import feedback
import faq
feedback.provide_feedback()
Room_Boking.booking()
faq.FAQ()

# import mysql.connector as sqlcon
# con=sqlcon.connect(host="localhost",user="root",passwd="12345",database='',auth_plugin="mysql_native_password")
# cursor=con.cursor()

print(con.is_connected())