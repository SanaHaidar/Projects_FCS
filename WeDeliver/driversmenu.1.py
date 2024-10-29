'''def drivers_menu():
     DISPLAY:
    "Drivers'Menu - Enter":
    "1.View All Drivers"
    "2.Add a driver"
    "3.Check Similar Drivers"
    "4.Go back to main menu"

    INPUT :
        IF INPUT = 1 :
            CALL ViewAllDrivers()
        IF INPUT =2 :
            CALL AddDrivers()
        IF INPUT = 3 : 
            CALL CheckSimilarDrivers()
        IF INPUT = 4 :
            CALL MAIN()
         
END FUNCTION'''


def drivers_menu():
    while True:
        print("Drivers'Menu - Enter:")
        print("1.View All Drivers")
        print("2.Add a driver")
        print("3.Check Similar Drivers")
        print("4.Go back to main menu")

        user_input = input("Please enter a valid option: ")
        if user_input.isdigit():
            user_input = int(user_input)
            if user_input == 1:
                view_all_drivers()
            elif user_input == 2:
                add_driver()
            elif user_input == 3:
                check_similar_drivers()
            elif user_input == 4:
                main()
            else:
                print("Invalid input, please enter a digit between 1 and 4 ")
        else:
            print("Invalid input, please enter a number : 1 , 2 , 3 or 4")


drivers_menu()
