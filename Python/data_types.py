# string data type

# Literal assignement
import math
first = 'Dave'
last = 'Gray'

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))


# construction function
# pizza = str("Pepperoni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))


# concatenation
fullname = first + ' ' + last
print(fullname)

fullname += "!"
print(fullname)

# casting a number to a string
decade = str(1980)
print(type(decade))
print(decade)

statement = "I like rock music from the " + decade + "s."
print(statement)

# multiple line
multiline = '''
Hey, how are you ?

I was just checking in.
                              All good?
'''
print(multiline)

# escaping special characters
sentence = 'I\'m back at work! \t HEY! \n\nWhere\'s at\\located? '
print(sentence)

# String Methods

print(first)
print(first.lower())
print(first.upper())
print(first)


print(multiline.title())
print(multiline.replace("good", "ok"))
print(multiline)


print(len(multiline))
multiline += "                                 "
multiline = "                            " + multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

print("")

# build a menu
title = "menu".upper()
print(title.center(20, "="))

print('Coffee'.ljust(16, ".") + "$1".rjust(4))
print('Muffin'.ljust(16, ".") + "$2".rjust(4))
print('CheeseCake'.ljust(16, ".") + "$4".rjust(4))
print("")

# string index value
print(first[1])
print(first[-1])
print(first[1:])

print("")
# Some methods return Boolean data
print(first.startswith("D"))
print(first.endswith("Z"))

print("")
# Boolean data type
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))


print("")
# Numeric Data Type
# integer
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

print("")
# float
gpa = 3.28
y = float(1.14)
print(type(gpa))
print(isinstance(y, float))

# complex type
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)


# Built-in functions
print(abs(gpa))
print(abs(gpa * -1))
print(round(gpa))
print(round(gpa, 1))

print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))


# Casting a string to a number
zipcode = "10001"
zip_value = int(zipcode)
print(type(zip_value))
