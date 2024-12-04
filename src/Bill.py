#Jai mata di
def bill( name= "jeb" , email="xyz@gmail.com" , phone=9876543210 , check_in=3 , check_out=7 , priceOfOneDay = 4):
      price = priceOfOneDay * (check_out - check_in)
    #   wil be calc via sql
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

     
    #def print_fancy_bill(name, email, phone, check_in, check_out, price):
    #print("\n" + "★" * 40)
    #print("🌟         HOTEL BOOKING BILL         🌟")
    #print("★" * 40)
    #print(f"👤  Customer Name   : {name}")
    #print(f"✉️  Email Address   : {email}")
    #print(f"📞  Phone Number    : {phone}")
    #print(f"🛏️  Check-In Date   : {check_in}")
    #print(f"🏁  Check-Out Date  : {check_out}")
    #print(f"💰  Total Amount    : ₹{total_Print}")
    #print("★" * 40)
    #print("✨  Thank you for booking with us!  ✨")
    #print("★" * 40)