
'''drivers = {"start_city": [{"ID": "", "name": ""}]}
cities = []


def view_all_drivers(drivers):
    for city, driver_list in drivers:
        for driver in drivers_list:
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


END def add_driver()


def check_similar_drivers(drivers):
    for city, driver_list in drivers:
        DISPLAY city: ADD(driver.name for driver in drivers_list)"
    END for
    DISPLAY "Return to Main Menu? (yes to return)"
    INPUT
    if INPUT = "yes":
        CALL main_menu()
    END if
END def check_similar_drivers()'''


drivers = {
    "Akkar": [{"ID": "ID001", "name": "Max Verstappen"}],
    "Saida": [{"ID": "ID002", "name": "Charles Leclerc"}],
    "Jbeil": [{"ID": "ID003", "name": "Lando Norris"}]
}
cities = {
    "Beirut": ["Jbeil"],
    "Jbeil": ["Akkar", "Beirut"],
    "Akkar": ["Jbeil"],
    "Saida": ["Zahle"],
    "Zahle": ["Saida"]
}


def view_all_drivers(drivers):
    for start_city, driver_list in drivers.items():
        for driver in driver_list:
            print(f'ID: {driver["ID"]},Name: {
                  driver["name"]}, Start City: {start_city}')


def add_driver(drivers, cities):
    name = input("Enter driver's name: ").strip()
    start_city = input("Enter start city: ").strip().lower()

    if start_city in cities:
        id = max(
            (int(driver["ID"][2:]) for start_city,
             driver_list in drivers.items() for driver in driver_list),
            default=0
        ) + 1
        id_new = f'ID{id+1:03}'
        driver_new = {"ID": id_new, "name": name}

        if start_city not in drivers:
            drivers[start_city] = []

        drivers[start_city].append(driver_new)
        print(f"{driver_new} added successfully")

    else:
        answer = input("The city is not available, add it? (yes/no)")

        if answer.lower() == "yes":

            cities[start_city] = []
            drivers[start_city] = []
            add_driver(drivers, cities)
        else:
            print("Driver was not added.")


def check_similar_drivers(drivers):
    for city, driver_list in drivers.items():
        print(city.capitalize() + ":" +
              ",".join(driver["name"]for driver in driver_list))
