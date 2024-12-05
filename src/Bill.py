def bill(cid,name, email, phone, check_in, check_out, priceOfOneDay):
      import mysql.connector as sqlcon
      con=sqlcon.connect(host="localhost",user="root",passwd="12345",database='swaraj_hotel',auth_plugin="mysql_native_password")
      cursor=con.cursor()
      q="select datediff('{}', '{}')days from customerinfo where c_id = {}".format(check_out,check_in,cid)
      cursor.execute(q)
      days= cursor.fetchall()
      con.commit()
      price = priceOfOneDay *(days[0][0])
      print(
            '''
            ★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★
            🌟  SWARAJ  HOTEL BILL  🌟
            ★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★
            👤  Customer Name   : {}                            
            ✉️  Email Address   : {}                            
            📞  Phone Number    : {}                            
            🛏️  Check-In Date   : {}                            
            🏁  Check-Out Date  : {}                            
            💰  Total Amount    : {}                            
            ★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★
            ✨  Thank you for booking with SWARAJ!  ✨
            ★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★
            
            '''.format(name,email,phone,check_in,check_out,price))
