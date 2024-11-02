'''Show cities
Print a list with the name of all the cities in the program sorted by descending alphabetical orders (From Z to A)
Search city
The user is asked to input a key, and the system will output all the city names that contain this key
For example, if the user inputs “ei”, the system would print “Jbeil, Beirut”
Print neighboring cities
Asks the user for a city name, and then prints all cities that can be reached from the user input.
Print Drivers delivering to city
Asks the users for a city name, and then prints all drivers that are delivering to this city. Drivers might not have this city as their starting city, but they can reach it by going through different cities.
 For example, if the user inputs Beirut, Both Max and Charles will be printed. But if the user inputs Zahle, only Lando will be printed.
Hint:
There are functions called “Breadth First Search (BFS)” and “Depth First Search (DFS)”, you can look them up and use them here. But you don’t have to.'''


def show_cities():
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


END def dirvers_delivering():
