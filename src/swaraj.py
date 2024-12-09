import Room_Booking
import Bill
import feedback
import misc
import faq
import room_perks
import staff_details
import rooms

def userPanel():
    while True:
        print('user panel')
        print('1. Book a Room')
        print('2. Cancel a Booking')
        print('3. View Room Details')
        print('4. provide a Feedback')
        print('5. FAQs')
        print('6. Get Your Bill')

        n = int(input('Enter your choice:'))
        
        if n==1:
            Room_Booking.room_booking()
        elif n==2:
            Room_Booking.cancelBooking()
        elif n==3:
            room_perks.perks()
        elif n==4:
            feedback.provide_feedback()
        elif n==5:
            faq.FAQ()
        elif n==6:
            Bill.billGenerator()
        else:
            continue
        exit=int(input("enter any number to continue and 2 to exit"))
        if exit==2:
            break

def admin():
    passwd = input('Enter your password:')
    if passwd=='admin':
        while True:
            print('Welcome Admin')
            print('1.View Feedback')
            print('2.View Rooms')
            print('3.View Customers')
            print('4.View Staff Details')
            print('5.Add New Staff Member')

            n = int(input('Enter your choice:'))
            if n==1:
                feedback.viewFeedBack()
            elif n==2:
                rooms.viewRooms()
            elif n==3:
                Room_Booking.viewCustomers()
            elif n==4:
                staff_details.staffDetails()
            elif n==5:
                staff_details.addStaff()
            else:
                continue
            exit=int(input("enter any number to continue and 2 to exit"))
            if exit==2:
                break
          
    else:
        print('wrong password try again')
        admin()



print("*****************************************")
print("*                                       *")
print("*     🌟 Welcome to Swaraj Hotel 🌟    *")
print("*            New Delhi, India           *")
print("*                                       *")
print("*****************************************")
print("****Created by Devanshu ,Vivek ,Kunal****")
print("*****************************************")

print('What would you like to do?')
print('1. user panel')
print('2. admin panel')

n = int(input('Enter your choice:'))
if n==1:
    userPanel()
elif n==2:
    admin()
else:
    misc.correct()


        