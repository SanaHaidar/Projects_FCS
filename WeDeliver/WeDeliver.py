from collections import deque


drivers = {
    "akkar": [{"ID": "ID001", "name": "Max Verstappen"}],
    "saida": [{"ID": "ID002", "name": "Charles Leclerc"}],
    "jbeil": [{"ID": "ID003", "name": "Lando Norris"}]
}
cities = {
    "beirut": ["jbeil"],
    "jbeil": ["akkar", "beirut"],
    "akkar": ["jbeil"],
    "saida": ["zahle"],
    "zahle": ["saida"]
}


def main():
    while True:
        print("\n\nHello! Please enter:")
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


def drivers_menu():
    while True:
        print("\n\nDrivers'Menu - Enter:")
        print("1.View All Drivers")
        print("2.Add a driver")
        print("3.Check Similar Drivers")
        print("4.Go back to main menu")

        user_input = input("Please enter a valid option: ")
        if user_input.isdigit():
            user_input = int(user_input)
            if user_input == 1:
                view_all_drivers(drivers)
            elif user_input == 2:
                add_driver(drivers, cities)
            elif user_input == 3:
                check_similar_drivers(drivers)
            elif user_input == 4:
                main()
            else:
                print("Invalid input, please enter a digit between 1 and 4 ")
        else:
            print("Invalid input, please enter a number : 1 , 2 , 3 or 4")


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
        answer = input(
            "The city is not available, add it? (yes/no)").strip().lower()

        if answer == "yes":
            cities[start_city] = []
            drivers[start_city] = []
            add_driver(drivers, cities)
        else:
            print("Driver was not added.")


def check_similar_drivers(drivers):
    for city, driver_list in drivers.items():
        print(city.capitalize() + ":" +
              ",".join(driver["name"]for driver in driver_list))


def cities_menu():
    while True:
        print("\n\n Cities Menu - Enter:")
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
            elif answer == 5:
                main()
                return
            else:
                print("Invalid input, please enter a digit between 1 and 4 ")
        else:
            print("Invalid input, please enter a number : 1 , 2 , 3 or 4")


def show_cities():
    sorted_cities = sorted(cities.keys(), reverse=True)
    for city in sorted_cities:
        print(city.capitalize())


def search_cities():
    key = input("\nEnter search key :").strip().lower()
    cities_key = [city.capitalize() for city in cities if key in city]
    if cities_key:
        print(f"Cities containing '{key}': {','.join(cities_key)}")
    else:
        print(f"No cities found containing '{key}' ")


def neighboring_cities():
    city = input("\nEnter city name").strip().lower()
    if city in cities:
        neighboring_cities = cities[city]
        if neighboring_cities:
            print(f"Neighboring cities to '{city}': {
                  ','.join(neighboring_cities)}")
        else:
            print(f"No Neighboring cities to '{city}'.")
    else:
        print("City not registered")


def bfs(start_city, visited, drivers_delivering):
    queue = deque([start_city])
    visited.add(start_city)

    while queue:
        current = queue.popleft()

        if current in drivers:
            for driver in drivers[current]:
                drivers_delivering.add(driver["name"])

        for neighbor in cities.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


def drivers_delivering():
    city = input("\nEnter city name: ").strip()
    visited = set()
    drivers_delivering = set()
    if city in cities:
        bfs(city, visited, drivers_delivering)
        if drivers_delivering:
            print(f"\n Driversdelivering to {city}:{
                  ','.join(drivers_delivering)}")
        else:
            print(f"No drivers found delivering to {city.capitalize()}.")
    else:
        print("City not registered")


main()
