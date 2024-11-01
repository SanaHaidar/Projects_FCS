CITIES’ MENU
In that menu, the user is given the following choices:
1. Show cities
2. Search city
3. Print neighboring cities
4. Print Drivers delivering to city


def Citiesmenu()


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


END FUNCTION
