'''View all drivers
A list of all the drivers and their details are printed to the users.
ID, driver's name, start_city

Add a driver

The user is asked to enter the name and start city of the driver
the driver is then saved to the
system.
The user does not input the ID of the driver, it is automatically generated by the
system
The user might input an invalid start city, make sure that the start city is already available
in the database.
If the city is not available,
ask the user if they want to add it to the
database,
if yes, you should do so.

Check similar drivers
Similar drivers are drivers that start off from the same city.
When the user chooses this option,
the system will print all the drivers that start off from the same city on the same line
Example:
City1: driver1, driver2
City2: driver 3
City3: driver4, driver5
Go back
This option takes the user back to the previous main menu.'''

drivers = {"start_city": [{"ID": "", "name": ""}]}
cities = []


def view_all_drivers(drivers):
    for city, driver_list in drivers:
        for driver in drivers:
            DISPLAY  "ID:", driver, ID "Name:", driver.name, "Start City:" driver.start_city
        END for
    END for


END def view_all_drivers():


def add_driver(drivers, cities):
    Prompt: "Enter driver's name:"
    INPUT name
    Prompt: "Enter start city:"
    INPUT start_city

    if start_city in cities:
        GENERATE Id for new driver

        if start_city not in drivers:
            drivers[start_city] = []
        ADD(ID, name, start_city) to drivers[start_city] = []

    else:
        Prompt: "The city is not available, add it? (yes/no)"
        INPUT answer
        if answer == "yes":
            ADD start_city to cities
            CALL add_driver(drivers, cities)
        else:
            RETURN to drivers_menu()

        END if
    END if


END def add_driver():


def check_similar_drivers(drivers):
    for city, driver_list in drivers:
        DISPLAY city: ADD(driver.name for driver in drivers_list)"
    END for 
END def check_similar_drivers()
            