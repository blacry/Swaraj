def FAQ():
    print("please enter your choice:")
    choice=int(input())

    a=input("Refund Policy:  PRESS 1")
    a=input("If you are not satisfied with your experience at Swaraj Hotel, you can return your booking and get a full refund of the amount paid. PRESS 2")
    a=input("Cancellation Policy: PRESS 2")
    a=input("You can cancel your booking at any time by contacting us through our contact details provided on our website or by calling us at +91-9876543210. PRESS 3")
    a=input("Terms and Conditions: PRESS 4")
    a=input("By using our website or mobile application, you agree to our Terms and Conditions. These Terms and Conditions outline the rules and regulations that govern your use of our website or mobile application. PRESS 5")
    a=input("Privacy Policy: PRESS 6")
    a=input("We value your privacy and are committed to protecting your personal information. Our Privacy Policy outlines the types of personal information we collect, how we use it, and how we protect it. PRESS 7")
    a=input("Help Center: PRESS 8")
    a=input("If you have any questions or need assistance, you can visit our Help Center for guidance. PRESS 9")

    if a==1:
        '''
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

    elif a==2:
        '''At Swaraj Hotel, your satisfaction is our top priority. We believe in providing a memorable and delightful experience for all our guests.
          However, if for any reason you are not satisfied with your stay, we offer a hassle-free refund policy to ensure your peace of mind.

          For more information, please refer to our refund policy.
        '''
    elif a==3:
        '''At Swaraj Hotel, we understand that sometimes things don't go as planned. We want to make sure you have a positive experience and that you are satisfied with your stay.
          If you have any issues or concerns, please don't hesitate to contact us. Our customer service team is always available to assist you.

          For more information, please refer to our cancellation policy.
        '''
    elif a==4:
        '''At Swaraj Hotel, we believe in providing a memorable and delightful experience for all our guests. We strive to make sure that our guests have a positive experience and that they are satisfied with their stay.
          However, if for any reason you are not satisfied with your experience, we offer a hassle-free refund policy to ensure your peace of mind.

          For more information, please refer to our terms and conditions.
        '''
    elif a==5:
        '''At Swaraj Hotel, we value your privacy and are committed to protecting your personal information. We understand that you may have concerns about how your information is being used and shared.
          We take your privacy seriously and are committed to ensuring that your personal information is kept confidential and secure.

          For more information, please refer to our privacy policy.
        '''
    elif a==6:
        '''At Swaraj Hotel, we value your privacy and are committed to protecting your personal information. We understand that you may have concerns about how your information is being used and shared.
          We take your privacy seriously and are committed to ensuring that your personal information is kept confidential and secure.

          For more information, please refer to our help center.
        '''
    elif a==7:
        '''At Swaraj Hotel, we value your privacy and are committed to protecting your personal information. We understand that you may have concerns about how your information is being used and shared.
          We take your privacy seriously and are committed to ensuring that your personal information is kept confidential and secure.

          For more information, please refer to our contact us.
        '''
    elif a==8:
        '''At Swaraj Hotel, we understand that sometimes things don't go as planned. We want to make sure you have a positive experience and that you are satisfied with your stay.
          If you have any issues or concerns, please don't hesitate to contact us. Our customer service team is always available to assist you.

          For more information, please refer to our help center.
        '''
    elif a==9:
        '''At Swaraj Hotel, we understand that sometimes things don't go as planned. We want to make sure you have a positive experience and that you are satisfied with your stay.
          If you have any issues or concerns, please don't hesitate to contact us. Our customer service team is always available to assist you.

          For more information, please refer to our contact us.'''
    else:
        print("Please enter a valid choice.")

FAQ()