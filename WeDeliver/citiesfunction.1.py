
'''def show_cities():
    SORT cities in descending alphabetical order
    DISPLAY cities


END def show_cities():


def search_cities():
    PROMPT "Enter search key :"
    INPUT key
    FILTER cities for cities containing key(list comprehension)
    DISPLAY key_cities


END def search_cities():


def neighboring_cities():
    PROMPT "Enter city name"
    INPUT city
    if city in cities:
        DISPLAY all neighboring cities OF city(value of the key)
    else:
        DISPLAY "City not registered"


END def neighboring_cities():


def dirvers_delivering():
    PROMPT "Enter city name"
    INPUT city
    if city in cities:
        FIND drivers who can deliver to city(using BFS or DFS)
        DISPLAY found_drivers
    else:
        DISPLAY "City not registered"


END def dirvers_delivering():'''
from collections import deque
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


def show_cities():
    sorted_cities = sorted(cities.keys(), reverse=True)
    for city in sorted_cities:
        print(city)


def search_cities():
    key = input("Enter search key :").strip().lower()
    cities_key = [city for city in cities if key in city]
    if cities_key:
        print(f"Cities containing '{key}': {','.join(cities_key)}")
    else:
        print(f"No cities found containing '{key}' ")


def neighboring_cities():
    city = input("Enter city name").strip().lower()
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

    city = input("Enter city name: ").strip().lower()
    visited = set()
    drivers_delivering = set()

    if city in cities:
        bfs(city, visited, drivers_delivering)
        if drivers_delivering:
            print(f"\n Driversdelivering to {city}:{
                  ','.join(drivers_delivering)}")
        else:
            print(f'No drivers found delivering to {city.capitalize()}')
    else:
        print("City not registered.")
