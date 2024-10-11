# Write a program that takes two integers from the user and outputs the range of values from this list
'''
list1 = [54, 76, 2, 4, 98, 100]
sorted_list = sorted(list1)


def valid_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if 0 <= value <= 100:
                return value
            else:
                print("Input must be between 0 and 100.Please try again.")
        except ValueError:
            print("Please enter a valid integer.")


a = valid_integer(("Choose an integer between 0 and 100: "))
b = valid_integer(("Choose an integer between 0 and 100: "))

start = min(a, b)
end = max(a, b)

values = [i for i in sorted_list if start <= i <= end]
print(f"The valies in the sorted list between {start} and {end} are: {values}")

'''
# Write a program that repeatedly asks the user for a letter, and then prints all the names in this list that contain that letter.
'''
Names = ["Maria", "Hala", "Ghady", "Ehsan", "Joe", "Zoe"]


def valid_input(prompt):
    while True:
        value = input(prompt)
        if value == "exit":
            return None
        if len(value) == 1 and value.isalpha():
            return value.lower()
        else:
            print("Input must be single letter.")


while True:
    user_input = valid_input(
        "Please enter a single letter or type 'exit' to quit: "
    )

    if user_input is None:
        print("Exiting the program. Goodbye!")
        break
    result = [i for i in Names if user_input in i.lower()]
    if result:
        print(f"Names containing '{user_input}' :{','.join(result)}")
    else:
        print(f"No names found containing '{user_input}'.")
    print()
'''

# Given this list: numbers = [-12, 4, 12, 25, 67], write a program that repeatedly asks the user to input a number, and then insert that number in its correct position in the list. And then print thelist. Keep asking the user to input a number until they input the value -99.
'''
numbers = [-12, 4, 12, 25, 67]
copy = sorted(numbers)


def valid_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid number.")


while True:
    a = valid_input(("Choose a number or -99 to exit : "))
    if a == -99:
        break
    copy.append(a)
    copy.sort()
    print(" the new list is :", copy)
    '''

# Given this string
# words = ”Is this the real life? Is this just fantasy? Caught in a landslide,no escape from reality Open your eyes, look up to the skies and see I'm justa poor boy, I need no sympathy Because I'm easy come, easy go, little high,little low Any way the wind blows doesn't really matter to me, to me Mama,just killed a man Put a gun against his head, pulled my trigger, now he'sdead Mama, life had just begun But now I've gone and thrown it all away Mama ooh, didn't mean to make you cry If I'm not back again this time tomorrowCarry on, carry on as if nothing really matters Too late, my time has come Sends shivers down my spine, body's aching all the time Goodbye, everybody, I've got to go Gotta leave you all behind and face the truth Mama, ooh (anway the wind blows) I don't wanna die I sometimes wish I'd never been born atall I see a little silhouetto of a man Scaramouche, Scaramouche, will you do the Fandango? Thunderbolt and lightning, very, very frightening me (Galileo)Galileo, (Galileo) Galileo, Galileo Figaro, magnifico But I'm just a poorboy, nobody loves me He's just a poor boy from a poor family Spare him hislife from this monstrosity.Ask the user for two integer values and print the slice of words that fall between these numbers. Makesure these numbers are valid and will not cause errors or weird outputs.Example: int1=3 int2=6 The output would be: this

'''
words = " Is this the real life? Is this just fantasy? Caught in a landslide,no escape from reality Open your eyes, look up to the skies and see I'm justa poor boy, I need no sympathy Because I'm easy come, easy go, little high,little low Any way the wind blows doesn't really matter to me, to me Mama,just killed a man Put a gun against his head, pulled my trigger, now he'sdead Mama, life had just begun But now I've gone and thrown it all away Mama ooh, didn't mean to make you cry If I'm not back again this time tomorrowCarry on, carry on as if nothing really matters Too late, my time has come Sends shivers down my spine, body's aching all the time Goodbye, everybody, I've got to go Gotta leave you all behind and face the truth Mama, ooh (anway the wind blows) I don't wanna die I sometimes wish I'd never been born atall I see a little silhouetto of a man Scaramouche, Scaramouche, will you do the Fandango? Thunderbolt and lightning, very, very frightening me (Galileo)Galileo, (Galileo) Galileo, Galileo Figaro, magnifico But I'm just a poorboy, nobody loves me He's just a poor boy from a poor family Spare him hislife from this monstrosity."
words_list = words.split()

def valid_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid number.")


a = valid_input("Choose an integer: ")
b = valid_input("Choose an integer: ")
words_list = words.split()

index = abs(a-b)

if index < len(words_list):
    result = words_list[index]
    print(f"The word at{index} is: {result}")
else:
    print("Index out of range")
'''
