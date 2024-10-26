# Write the recursive version of binary search.


def binarySearch(list1, i, start, end):
    if end >= start:
        mid = (start+end)//2
        if list1[mid] == i:
            return mid
        elif list1[mid] > i:
            return binarySearch(list1, i, 0, mid-1)
        else:
            return binarySearch(list1, i, mid+1, end)
    else:
        return -1


list1 = [2, 3, 4, 10, 40]
i = 10
result = binarySearch(list1, i, 0, len(list1)-1)
if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not found")

print("")
print("")
print("")

# Given a list of characters and an integer n, generate, using recursion, all possible combinations of length n that contain the characters in the list.


def generateCombinations(characters, n, str1):
    if n == 0:
        print(str1)
        return
    for element in characters:
        generateCombinations(characters, n-1, str1+element)


characters = ["a", "b", "c"]
generateCombinations(characters, 2, "")

print("")
print("")
print("")

# Given a sorted list of integers, and an integer value, add value to the correct position of the list.


def addValue(list1, value, start, end):
    if start >= end:
        list1.insert(start, value)
        return list1
    mid = (start+end)//2
    if list1[mid] > value:
        return addValue(list1, value, start, mid)
    elif list1[mid] < value:
        return addValue(list1, value, mid+1, end)
    else:
        list1.insert(mid+1, value)
        return list1


list1 = [2, 8, 34, 67, 99]
value = 34
result = addValue(list1, value, 0, len(list1))
print(result)

print("")
print("")
print("")

# You want to write a POS system (point of service) to your neighbor’s dekene.In this system, you keep track of the items available. The items have a barcode, a name, and aprice.When the system starts, it asks your 3ammo l dekanje if he wants to start a new receipt.If he chooses yes, he will be prompted for an item barcode and the quantity the clientpurchased. If he answers no, the system exits.After choosing “yes” and then inputting the barcode and the quantity, aamo l dekanje is asked ifhe would like to add another item to the list. If he answers yes, he is prompted again for the barcode and quantity of the item. He will keep getting this prompt until he answers no to the question. Once he answered no, you the system will display the receipt where each item will appear on a line along with the quantity purchased and the total cost of that item (quantity*unit price) and at the last line of the receipt, the system prints the total along with the total amount. Once this receipt is printed, the system goes back to the first step and asks aamo l dekane if he would like to start a new receipt.

items = {
    "123456": {"name": "Cupcake", "price": 30},
    "234567": {"name": "Cheesecake", "price": 120},
    "345678": {"name": "Juice", "price": 20},
    "456789": {"name": "Darkblue", "price": 50},
    "536789": {"name": "Snips", "price": 30},
    "454589": {"name": "Master", "price": 30}
}


def askReceipt():
    while True:
        purchase = input(
            "Do you want to start a new receipt? (yes/no): ").strip().lower()

        if purchase not in ("yes", "no"):
            print("This option is unavailable. Please choose 'yes' or 'no'.")
        elif purchase == "no":
            print("Exiting the system.")
            return
        else:
            handleReceipt()


def handleReceipt():
    receipt = []

    while True:
        barcode = input("Enter the barcode of the item you want: ").strip()

        if barcode not in items:
            print("Barcode not found. Please try again.")
            continue

        item_name = items[barcode]["name"]
        item_price = items[barcode]["price"]
        print(f"Item chosen: {item_name} (Price: {item_price})")

        while True:
            try:
                quantity = int(input(f"Enter the quantity of {item_name}: "))
                if quantity <= 0:
                    print("Quantity must be a positive integer.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

        item_total = quantity * item_price
        receipt.append({"name": item_name, "quantity": quantity,
                       "unit_price": item_price, "total_price": item_total})

        more_items = input(
            "Would you like to add another item? (yes/no): ").strip().lower()
        if more_items == "no":
            printReceipt(receipt)
            return


def printReceipt(receipt):
    total_amount = 0
    print("\n--- Receipt ---")

    for item in receipt:
        name = item["name"]
        quantity = item["quantity"]
        unit_price = item["unit_price"]
        total_price = item["total_price"]

        print(f"{name}: {quantity} x {unit_price} = {total_price}")
        total_amount += total_price

    print(f"Total amount: {total_amount}")
    print("--- End of Receipt ---\n")


askReceipt()
