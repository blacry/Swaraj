def staffDetails():
    import mysql.connector as sqlcon
    con=sqlcon.connect(host="localhost",user="root",passwd="12345",database='swaraj_hotel',auth_plugin="mysql_native_password")
    cursor=con.cursor()
    query="select * from staffinfo"
    cursor.execute(query)
    for i in cursor.fetchall():
        print(i)
def s_id():
    
    import random
    import mysql.connector as sqlcon
    sid=random.randint(1,1000)

    con=sqlcon.connect(host="localhost",user="root",passwd="12345",database='swaraj_hotel',auth_plugin="mysql_native_password")
    cursor=con.cursor()

    check = "select s_id from staffinfo where s_id ={}".format(sid)
    cursor.execute(check)
    check = cursor.fetchall()

    if check:
         sid = s_id()
    return sid

def addStaff():
    sid = s_id()
    while True:
        print('Enter your details')
        name = input('Enter your name: ').strip()
        if not name:
            print("Name cannot be empty. Please try again.")
            continue
        
        email = input('Enter your email address: ').strip()
        if not ("@gmail.com" in email):
            print("Please enter a valid Gmail address.")
            continue

        phone = input('Enter your phone number (10 digits): ').strip()
        if not (phone.isdigit() and len(phone) == 10 and int(phone) != 0):
            print("Invalid phone number! Please enter a correct number.")
            continue
        age = input('Enter your age: ').strip()
        if not age.isdigit():
            print("Invalid input! Please enter a valid number")
            continue
        elif int(age) < 18:
            print("Your age cannot be less than 18")
            continue
        gender = input('Enter your gender (M/F/O): ').strip()
        if gender not in ['M','F','O']:
            print("Invalid input! Please enter a valid gender")
            continue
        postion = input('Enter your position: ').strip()
        if not postion:
            print("Position cannot be empty. Please try again.")
            continue

        address = input('Enter your address: ').strip()
        if not address or len(address) < 50:
            print("Address cannot be empty. Please try again.")
            continue

        print("Thank you for providing your details")

        import mysql.connector as sqlcon
        con=sqlcon.connect(host="localhost",user="root",passwd="12345",database='swaraj_hotel',auth_plugin="mysql_native_password")
        cursor=con.cursor()

        query="insert into staffinfo values({},'{}',{},'{}','{}','{}','{}',{})".format(sid,name,int(age),gender,postion,email,address,phone)
        cursor.execute(query)
        con.commit()

        cursor.close()
        con.close()