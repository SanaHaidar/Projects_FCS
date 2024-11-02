
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
    key = input("Enter search key :").strip()
    cities_key = [city for city in cities.keys()if key in city]
    if cities_key:
        print(f"Cities containing '{key}': {','.join(cities_key)}")
    else:
        print(f"No cities found containing '{key}' ")


def neighboring_cities():
    city = input("Enter city name").strip()
    if city in cities:
        neighboring_cities = cities[city]
        if neighboring_cities:
            print(f"Neighboring cities to '{city}': {
                  ','.join(neighboring_cities)}")
        else:
            print(f"No Neighboring cities to '{city}'.")
    else:
        print("City not registered")
