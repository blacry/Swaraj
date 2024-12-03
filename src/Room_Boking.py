import correction
def room_booking():
    print('What kind of room do you want to book?')
    print('1.Single Room')
    print('2.Double Room')
    print('3.Twin Room')
    print('4.Family Room')

    room_choice=int(input('Enter your choice:'))
    price = priceDetails(room_choice)

    coustomer_email,coustomer_phone,coustomer_check_in,coustomer_check_out = coustomerDetails()

def staff_details():
    print('coming soon')

def booking():    
    print('======================Welcom to SWARAJ======================')
    print('1. Book a Room')
    print('2. See Staff Details')

    to_do_choice = int(input('Enter your choice:'))

    if to_do_choice == 1:
        room_booking()
    elif to_do_choice == 2:
        staff_details()
    else:
        correction.correct(booking)
        
def coustomerDetails():
    print('Enter your details:')
    print('Enter the email address:')
    email=input()
    print('Enter the phone number:')
    phone=input()
    print('Enter the check in date:')
    check_in=input()
    print('Enter the check out date:')
    check_out=input()
    return email,phone,check_in,check_out

def priceDetails(choice):
    if choice==1:
        a = input('Your room will be of ₹ 1000 , Press 1 to confirm ')
        if int(a) == 1:
            return 1000
        else:
            priceDetails(choice)

    if choice==2:
        a = input('Your room will be of ₹ 2000 , Press 1 to confirm ')
        if int(a) == 1:
            return 2000
        else:
            priceDetails(choice)

    if choice==3:
        a = input('Your room will be of ₹ 4000 , Press 1 to confirm ')  
        if int(a) == 1:
            return 4000
        else:
            priceDetails(choice)

    if choice==4:
        a = input('Your room will be of ₹ 6000 , Press 1 to confirm ')
        if int(a) == 1:
            return 6000
        else:
            priceDetails(choice)
    else:
        correction.correct(room_booking)


'''
    def bookRoom(room_no,name,email,phone,address,room_type,price,check_in,check_out,bill):
    con=sqlcon.connect(host="localhost",user="root",passwd="12345",database='',auth_plugin="mysql_native_password")
    cursor=con.cursor()
    cursor.execute("INSERT INTO room_booking(room_no,name,email,phone,address,room_type,price,check_in,check_out,bill) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(room_no,name,email,phone,address,room_type,price,check_in,check_out,bill))
    con.commit()
    cursor.close()
    con.close()
'''

'''
print('2.Check Room Availability')
print('3.Contact Us')
print('4.Provide Feedback')
print('5.View Feedback')
print('6.Exit')
choice=int(input('Enter your choice:'))
if choice==1:
    print('Enter the room number:')
    room_no=int(input())
    print('Enter the guest name:')
    name=input()
    print('Enter the age:')
    age=int(input())
    print('Enter the gender:')
    gender=input()
    print('Enter the email:')
    email=input()
    print('Enter the phone number:')
    phone=input()
    print('Enter the address:')
    address=input()
    print('Enter the room type:')
    room_type=input()
    print('Enter the price:')
    price=int(input())
    print('Enter the check in date:')
    check_in=input()
    print('Enter the check out date:')
    check_out=input()
    print('Enter the bill amount:')
    bill=int(input())
    print('Enter the feedback:')
    feedback=input()
    if feedback=='':
        print('Enter the feedback:')
        feedback=input()
    else:
        print('Thank you for providing feedback')
    con=sqlcon.connect(host="localhost",user="root",passwd="12345",database='',auth_plugin="mysql_native_password")
    cursor=con.cursor()
    cursor.execute("INSERT INTO room_booking(room_no,name,age,gender,email,phone,address,room_type,price,check_in,check_out,bill,feedback) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(room_no,name,age,gender,email,phone,address,room_type,price,check_in,check_out,bill,feedback))
    con.commit()
    cursor.close()
    con.close()
elif choice==2:
    print('Enter the room number:')
    room_no=int(input())
    con=sqlcon.connect(host="localhost",user="root",passwd="12345",database='',auth_plugin="mysql_native_password")
    cursor=con.cursor()
    cursor.execute("SELECT * FROM room_booking WHERE room_no=%s",(room_no))
    result=cursor.fetchall()
    for row in result:
        print('Room Number:',row[0])
        print('Name:',row[1])
        print('Age:',row[2])
        print('Gender:',row[3])
        print('Email:',row[4])
        print('Phone:',row[5])
        print('Address:',row[6])
        print('Room Type:',row[7])
        print('Price:',row[8])
        print('Check In:',row[9])
        print('Check Out:',row[10])
        print('Bill:',row[11])
        print('Feedback:',row[12])
    cursor.close()
    con.close()
elif choice==3:
    print('Email: swaraj@gmail.com')
    print('Phone: +91-9876543210')
elif choice==4:
    print('Enter the room number:')
    room_no=int(input())
    print('Enter the feedback:')
    feedback=input()
    if feedback=='':
        print('Enter the feedback:')
        feedback=input()
    else:
        print('Thank you for providing feedback')
    con=sqlcon.connect(host="localhost",user="root",passwd="12345",database='',auth_plugin="mysql_native_password")
    cursor=con.cursor()
    cursor.execute("UPDATE room_booking SET feedback=%s WHERE room_no=%s",(feedback,room_no))
    con.commit()
    cursor.close()
    con.close()
elif choice==5:
    print('Enter the room number:')
    room_no=int(input())
    con=sqlcon.connect(host="localhost",user="root",passwd="12345",database='',auth_plugin="mysql_native_password")
    cursor=con.cursor()
    cursor.execute("SELECT * FROM room_booking WHERE room_no=%s",(room_no))
    result=cursor.fetchall()
    for row in result:
        print('Room Number:',row[0])
        print('Name:',row[1])
        print('Age:',row[2])
        print('Gender:',row[3])
        print('Email:',row[4])
        print('Phone:',row[5])
        print('Address:',row[6])
        print('Room Type:',row[7])
        print('Price:',row[8])
        print('Check In:',row[9])
        print('Check Out:',row[10])
        print('Bill:',row[11])
        print('Feedback:',row[12])
    cursor.close()
    con.close()
elif choice==6:
    print('Thank you for using Swaraj Hotel')
    exit()
else:       
'''