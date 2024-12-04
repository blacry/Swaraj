def perks():
    print("""
    Perks of rooms based on their price ranges. Kindly select the range 
    off your room according to your room type
    """)
    room_perks={
        1:["Single Room","Single bed", "Free Wi-Fi", "Shared bathroom"],
        2:["Double Room","Double bed", "Private bathroom", "Flat-screen TV", "Free Wi-Fi"],
        3:["Twin Room","Two single beds", "Private bathroom", "Complimentary breakfast", "Free Wi-Fi"],
        4:["Family Room","Queen bed", "Ensuite bathroom", "Smart TV", "Mini-fridge", "Family lounge access"],
        5:["Luxury Room","King bed", "Luxury bathroom", "Smart TV", "Mini-bar", "Personal assistant", "Room service"]
    }
    
    print("What kind of room do you want to book?")
    print("1. Single Room")
    print("2. Double Room")
    print("3. Twin Room")
    print("4. Family Room")
    print("5. Luxury Room\n")
    
    try:
        choice = int(input("Enter the number corresponding to your choice (1-5): "))
        
        if choice in room_perks:
            print("You have selected a " + room_perks[choice][0])
            print("Here are the perks of this room:")
            for perks in room_perks[choice]:
                print("-{}".format(perks))
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")
    except ValueError:
        print("Invalid input! Please enter a valid number")
        