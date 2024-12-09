def provide_feedback():
    print('please provide us your valuable feedback')

    email = emailfxn()
    rating = ratingfxn()
    feedback = feedbackfxn()
    roomno = roomnofxn(email)
    
    insertFeedback(email, rating , feedback , roomno)

def emailfxn():
    while True:
        email=input("Enter your Email_id:")
        
        import mysql.connector as sqlcon
        con=sqlcon.connect(host="localhost",user="root",passwd="12345",database='swaraj_hotel',auth_plugin="mysql_native_password")
        cursor=con.cursor()

        cursor.execute('select email from customerinfo where email = "{}"'.format(email))
        query=cursor.fetchall()

        if not query:
            print("you have enetered wrong email \nplease enter the correct email id")
            continue
        else:
            return email   

def ratingfxn():
    ratings = input("Give us a rating from 1-5:")
    if ratings.isdigit():
        ratings = int(ratings)
    
    if ratings in range(1,6):
        print("Thank you for rating Swaraj Hotel!")
        return ratings
    else:
        print("""
              Please enter a valid rating\n""")
        ratingfxn()

def feedbackfxn():
    feedbacks=input("Enter your feedback:")

    if feedbacks=='':
        feedbackfxn()
    else:
        print("Thank you for providing feedback!")
        return feedbacks
    
def roomnofxn(email):
    print('Please enter the room number:')
    roomno=int(input())

    import mysql.connector as sqlcon
    con=sqlcon.connect(host="localhost",user="root",passwd="12345",database='swaraj_hotel',auth_plugin="mysql_native_password")
    cursor=con.cursor()

    cursor.execute('select * from customerinfo natural join roominfo where roomno = {} and email = "{}"'.format(roomno, email))
    room = cursor.fetchall()
    if room:
        return roomno
    else:
        print('Please enter your correct room number')
        roomnofxn(email)

def insertFeedback(email , rating, feedback , roomno) :

    import mysql.connector as sqlcon
    con=sqlcon.connect(host="localhost",user="root",passwd="12345",database='swaraj_hotel',auth_plugin="mysql_native_password")
    cursor=con.cursor()

    query = 'select c_id from customerinfo natural join roominfo where email = "{}" and roomno = {}'.format( email, roomno)
    cursor.execute(query)
    c_id=cursor.fetchall()
    c_id=c_id[0][0]
    insert = 'insert into feedback values({} , {}, "{}")'.format(c_id, rating, feedback)
    cursor.execute(insert)
    con.commit()
   
def viewFeedBack():

    import mysql.connector as sqlcon
    con=sqlcon.connect(host="localhost",user="root",passwd="12345",database='swaraj_hotel',auth_plugin="mysql_native_password")
    cursor=con.cursor()
    cursor.execute('select * from feedback')
    for i in cursor.fetchall(): 
        print(i)