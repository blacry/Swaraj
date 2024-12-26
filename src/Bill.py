# jai mata di
def bill(cid = 69696969, name = 'vivek', email = 'vivek@gmail.com', phone = '4545454545', check_in = '2024-12-05', check_out = '2024-12-15', priceOfOneDay = 7500 , room_no = 15):
      fh = open('bill-{}.txt'.format(cid),'w',encoding='UTF-8')

      import mysql.connector as sqlcon
      con = sqlcon.connect( host="sql12.freesqldatabase.com",user="sql12753911",passwd="vXHHHP8jFP",database='sql12753911',auth_plugin="mysql_native_password" )
      cursor=con.cursor()

      q="select datediff('{}', '{}')days from customerinfo where c_id = {}".format(check_out,check_in,cid)
      cursor.execute(q)
      days= cursor.fetchall()
      con.commit()

      price = priceOfOneDay  * days[0][0]

      a =('''
★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★
           🌟  SWARAJ  HOTEL BILL  🌟          
★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★
     📍  Customer ID     : {}                            
     🙍‍♂️  Customer Name   : {}                            
     ✉️  Email Address   : {}                            
     📞  Phone Number    : {}                            
     👣  Check-In Date   : {}                            
     🏁  Check-Out Date  : {}                            
     🛌  Room No.        : {}
     💰  Total Amount    : {}
★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★
   ✨  Thank you for booking with SWARAJ!  ✨
★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★'''.format(cid,name,email,phone,check_in,check_out,room_no,price))
      
      fh.write(a)
      fh.close()

def billGenerator():
      print('Enter your details')
      while True:
            cid = input('Enter your customer id: ').strip()
            try:
                  cid = int(cid)
            except ValueError:
                  print('Invalid input! Please enter a valid number')
                  continue

            import mysql.connector as sqlcon
            con = sqlcon.connect( host="sql12.freesqldatabase.com",user="sql12753911",passwd="vXHHHP8jFP",database='sql12753911',auth_plugin="mysql_native_password" )
            cursor=con.cursor()

            cursor.execute("select * from customerinfo where c_id = {}".format(cid))
            result=cursor.fetchall()
            if result:
                  customer_name, customer_email, customer_phone, customer_check_in, customer_check_out = result[0]
                  cursor.execute("select roomno and roomtype from roominfo where c_id = {}".format(cid))
                  data = cursor.fetchall()
                  if data:
                        roomno = data[0][0]
                        roomtype = data[0][1]
                        rooms = {
                              'Single Room':1000, 'Double Room':2000, 'Twin Room':4000, 'Family Room':6000, 'Luxuary Room':10000
                        }
                        price = rooms[roomtype]
                        bill(cid,customer_name,customer_email,customer_phone,customer_check_in,customer_check_out,price,roomno)
                        print('Thank you for booking with SWARAJ! Your Bill has been successfully generated')
                        break
                  else:
                        print('Customer not found')
                        continue
            else:
                  print('Customer not found')
                  continue