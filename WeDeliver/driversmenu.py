
DRIVERS’ MENU
In that menu, the user is greeted with the following options:
Enter:
1. To view all the drivers
2. To add a driver
3. Check similar drivers
4. To go back to the main menu


*pseudocode*


def drivers_menu():
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
         
END FUNCTION