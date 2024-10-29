'''*Pseudocode*
#Start:
    DISPLAY "Hello!Please enter":
    1."Go to Driver's Menu"
    2."Go to Cities' Menu"
    3."Exit"

    INPUT
       IF INPUT = 1:
            CALL DriversMenu()
        IF INPUT = 2:
            CALL CitiesMenu()
        IF INPUT = 3:
            EXIT

END '''


def main():
    while True:
        print("Hello! Please enter:")
        print("1.Go to Drivers'Menu")
        print("2.Go to Cities' Menu")
        print("3.Exiting the system")

        user_input = input("Please enter a valid option: ")
        if user_input.isdigit():
            user_input = int(user_input)
            if user_input == 1:
                drivers_menu()
            elif user_input == 2:
                cities_menu()
            elif user_input == 3:
                print("Exiting the system.")
                break
            else:
                print("Invalid input, please enter a digit between 1 and 3 ")
        else:
            print("Invalid input, please enter a number : 1 , 2 or 3")


main()
