'''def Citiesmenu()


DISPLAY:
    "Cities'Menu - Enter":
    "1.Show Cities"
    "2.Search City"
    "3.Print Neighboring City"
    "4.Print Drivers Delivering to City"

    INPUT:
        IF INPUT = 1:
            CALL ShowCities()
        IF INPUT = 2:
            CALL SearchCities()
        IF INPUT = 3:
            CALL NeighboringCities()
        IF INPUT = 4:
            CALL DriversDelivering()


END FUNCTION'''


def cities_menu():
    while True:
        print("\n Cities Menu - Enter:")
        print("1.Show Cities")
        print("2.Search Cities")
        print("3.Print Neighboring Cities")
        print("4.Print Drivers Delivering to City")

        answer = input("Enter:")
        if answer.isdigit():
            answer = int(answer)
            if answer == 1:
                show_cities()
            elif answer == 2:
                search_cities()
            elif answer == 3:
                neighboring_cities()
            elif answer == 4:
                drivers_delivering()
            else:
                print("Invalid input, please enter a digit between 1 and 4 ")
        else:
            print("Invalid input, please enter a number : 1 , 2 , 3 or 4")
