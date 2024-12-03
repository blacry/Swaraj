def provide_feedback():
    print('please provide us your valualbe feedback')
    email=input("Enter your Email_id:")
    #email lo sql se verify karna hai
    query = 'select email from coustomer where email = {}'.format(email)
    # emailcon.execute(query)
    rating = int(input("Give us a rating from 1-5:"))
    ratingfxn(rating)
    feedback=input("Enter your feedback:")
    feedbackfxn(feedback)

def ratingfxn(ratings):
    if ratings in range(1,6):
        print("Thank you for rating Swaraj Hotel!")
    else:
        print("""\n              Please enter a valid rating\n""")
        ratings=int(input("please give your rating:"))
        ratingfxn(ratings)

def feedbackfxn(feedbacks):
    if feedbacks=='':
        feedbacks=input("please give your feedback:")
        feedbackfxn(feedbacks)
    else:
        print("Thank you for providing feedback!")


# provide_feedback()
