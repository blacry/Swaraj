# jai mata di
def bill(cid,name, email, phone, check_in, check_out, priceOfOneDay , room_no):
      fh = open('{}bill.txt'.format(cid),'w',encoding='UTF-8')

      import mysql.connector as sqlcon
      con=sqlcon.connect(host="localhost",user="root",passwd="12345",database='swaraj_hotel',auth_plugin="mysql_native_password")
      cursor=con.cursor()

      q="select datediff('{}', '{}')days from customerinfo where c_id = {}".format(check_out,check_in,cid)
      cursor.execute(q)
      days= cursor.fetchall()
      con.commit()

      price = priceOfOneDay *(days[0][0])
      
      a =('''
     ★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★
     🌟  SWARAJ  HOTEL BILL  🌟
     ★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★
     🙍‍♂️  Customer Name   : {}                            
     ✉️  Email Address   : {}                            
     📞  Phone Number    : {}                            
     👣  Check-In Date   : {}                            
     🏁  Check-Out Date  : {}                            
     🛌  Room No.        : {}
     💰  Total Amount    : {}
     ★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★
     ✨  Thank you for booking with SWARAJ!  ✨
     ★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★
     
     '''.format(name,email,phone,check_in,check_out,room_no,price))
      
      fh.write(a)
      fh.close()

