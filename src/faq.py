import correction
def FAQ():

    print("Refund Policy:  PRESS 1")
    print("If you are not satisfied with your experience at Swaraj Hotel, you can return your booking and get a full refund of the amount paid. PRESS 2")
    print("Cancellation Policy: PRESS 3")
    print("You can cancel your booking at any time by contacting us through our contact details provided on our website or by calling us at +91-9876543210. PRESS 4")
    print("Terms and Conditions: PRESS 5")
    print("By using our website or mobile application, you agree to our Terms and Conditions. These Terms and Conditions outline the rules and regulations that govern your use of our website or mobile application. PRESS 5")
    print("Privacy Policy: PRESS 7")
    print("We value your privacy and are committed to protecting your personal information. Our Privacy Policy outlines the types of personal information we collect, how we use it, and how we protect it. PRESS 7")
    print("Help Center: PRESS ")
    print("If you have any questions or need assistance, you can visit our Help Center for guidance. PRESS 9")

    a=int(input("Please enter your choice:"))

    if a==1:
      a =  '''
     Refund Policy for Swaraj Hotel:

     --At Swaraj Hotel, we strive to provide a seamless experience for our valued guests. We understand that plans can change, and we aim to accommodate refund requests fairly and transparently. Below is our refund policy:

     1. Cancellation Timeframe and Refund Eligibility
     
     --Full Refund:
     Cancellations made more than 7 days before the check-in date will receive a full refund.
     
     --Partial Refund:
     Cancellations made between 3 to 7 days before the check-in date will be eligible for a 50% refund.
     
     --No Refund:
     Cancellations made less than 3 days before the check-in date will not be eligible for a refund.
     
     2. Non-Refundable Bookings
     Certain special promotions, last-minute deals, or discounted bookings are non-refundable. Guests are advised to review the terms of their booking before finalizing.
     
     3. Refund Process
     Refunds will be processed to the original payment method within 7-10 business days of the cancellation confirmation. The actual time for the refund to reflect in your account may vary depending on your bank or payment provider.
     '''
      print(a)

    elif a==2:
      a =  '''
          At Swaraj Hotel, your satisfaction is our top priority. We believe in providing a memorable and delightful experience for all our guests.
          However, if for any reason you are not satisfied with your stay, we offer a hassle-free refund policy to ensure your peace of mind.

          For more information, please refer to our refund policy.
        '''
      print(a)
    elif a==3:
      a =  '''
          At Swaraj Hotel, we understand that sometimes things don't go as planned. We want to make sure you have a positive experience and that you are satisfied with your stay.
          If you have any issues or concerns, please don't hesitate to contact us. Our customer service team is always available to assist you.

          For more information, please refer to our cancellation policy.
        '''
      print(a)
    elif a==4:
      a =  '''
          At Swaraj Hotel, we believe in providing a memorable and delightful experience for all our guests. We strive to make sure that our guests have a positive experience and that they are satisfied with their stay.
          However, if for any reason you are not satisfied with your experience, we offer a hassle-free refund policy to ensure your peace of mind.

          For more information, please refer to our terms and conditions.
        '''
      print(a)
    elif a==5:
      a =   '''
          At Swaraj Hotel, we value your privacy and are committed to protecting your personal information. We understand that you may have concerns about how your information is being used and shared.
          We take your privacy seriously and are committed to ensuring that your personal information is kept confidential and secure.

          For more information, please refer to our privacy policy.
        '''
      print(a)
    elif a==6:
      a =  '''
          At Swaraj Hotel, we value your privacy and are committed to protecting your personal information. We understand that you may have concerns about how your information is being used and shared.
          We take your privacy seriously and are committed to ensuring that your personal information is kept confidential and secure.

          For more information, please refer to our help center.
        '''
      print(a)
    elif a==7:
      a =  '''
          At Swaraj Hotel, we value your privacy and are committed to protecting your personal information. We understand that you may have concerns about how your information is being used and shared.
          We take your privacy seriously and are committed to ensuring that your personal information is kept confidential and secure.

          For more information, please refer to our contact us.
        '''
      print(a)
    elif a==8:
      a =  '''
          At Swaraj Hotel, we understand that sometimes things don't go as planned. We want to make sure you have a positive experience and that you are satisfied with your stay.
          If you have any issues or concerns, please don't hesitate to contact us. Our customer service team is always available to assist you.

          For more information, please refer to our help center.
        '''
      print(a)
    elif a==9:
      a =  '''
          At Swaraj Hotel, we understand that sometimes things don't go as planned. We want to make sure you have a positive experience and that you are satisfied with your stay.
          If you have any issues or concerns, please don't hesitate to contact us. Our customer service team is always available to assist you.

          For more information, please refer to our contact us.
          '''
      print(a)
    else:
        correction.correct(FAQ)
