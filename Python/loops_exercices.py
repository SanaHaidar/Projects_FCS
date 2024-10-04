# 1. Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included).
# nl = []
# for x in range(1500, 2701):
#     if (x % 7 == 0) and (x % 5 == 0):
#         nl.append(str(x))
# print(','.join(nl))


# # 2. Write a Python program to convert temperatures to and from Celsius and Fahrenheit.
# # [ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
# temp = input("What temperature would you like to convert?")
# degree = int(temp[:-1])
# temp_unit = temp[-1]
# if temp_unit.upper() == "C":
#     result = int(round((9*degree/5+32)))
#     new_temp_unit = "Fahrenheit"
# elif temp_unit.upper() == "F":
#     result = int(round((degree-32)*5/9))
#     new_temp_unit = "Celsius"
# else:
#     print("Input proper convention.")
#     quit()
# print("The temperatue in", new_temp_unit, "is", result, "degrees.")


# 5. Write a Python program that accepts a word from the user and reverses it.
word = input("What word would you like to reverse?")
for x in range(len(word) - 1, -1, -1):
    print(word[x], end="")
print('\n')
