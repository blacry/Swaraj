def roomfinder(roomtype):
  roomlist = {
    1:[1,21] , 2:[21,41] , 3:[41,61] , 4:[61,81] , 5:[81,101]
  }

  for i in range(roomlist[roomtype][0] , roomlist[roomtype][1]):
    import mysql.connector as sqlcon
    con=sqlcon.connect(host="localhost",user="root",passwd="12345",database='swaraj_hotel',auth_plugin="mysql_native_password")
    cursor=con.cursor()

    query="select roomno from roominfo where status='available' and roomno={}".format(i)
    cursor.execute(query)
    result=cursor.fetchall()
    if result:
      print("Your Room No. is{}".format(i))
      return i
    
def roomassigner (room_no,c_id,checkout):

    import mysql.connector as sqlcon
    con=sqlcon.connect(host="localhost",user="root",passwd="12345",database='swaraj_hotel',auth_plugin="mysql_native_password")
    cursor=con.cursor()
    query="update roominfo set c_id={} where roomno={}".format(c_id,room_no)
    cursor.execute(query)
    query="update roominfo set status='booked' where roomno={} and c_id={}".format(room_no,c_id)
    cursor.execute(query)
    query="update roominfo set checkout='{}' where roomno={} and c_id={}".format(checkout,room_no,c_id)
    cursor.execute(query)
    con.commit()
  
def viewRooms():
   
    import mysql.connector as sqlcon
    con=sqlcon.connect(host="localhost",user="root",passwd="12345",database='swaraj_hotel',auth_plugin="mysql_native_password")
    cursor=con.cursor()
    cursor.execute('select * from roominfo')
    for i in cursor.fetchall(): 
        print(i)