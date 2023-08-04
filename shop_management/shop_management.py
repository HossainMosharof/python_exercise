#Importing Items
import datetime
import os
import subprocess

#Global variables
grand_total = 0
current_datetime = datetime.datetime.now()

#Clearing the text file
open("purchase_history.txt", 'w').close()

#Clearing the console
def clear():
    if os.name == 'nt':  # For Windows
        subprocess.call('cls', shell=True)
    else:  # For other platforms (Linux, macOS)
        subprocess.call('clear', shell=True)


# List of items
items = {
    "bat": 1120,
    "ball": 50,
    "osaka": 30,
    "football": 690,
    "stamp": 70
}


def start():
    while True:
        user_data = input(
            "Which sports item you want to buy.\nType 'bat' , 'ball' , 'osaka' , 'football' or 'stamp'.\nType 'E' for Exit or 'T' for Total: ").lower()
        if user_data in items:
            return user_data
        elif user_data == 'e':
            return user_data
        elif user_data == 't':
            return user_data
        else:
            clear()
            print(f"Invalid Item. Please input a valid item")


def buying(name, price):
    global grand_total
    quantity = int(input(f"How many {name} you want to buy: "))
    total = quantity * price
    with open("purchase_history.txt", "a") as file:
        file.write(f"Total {name} price {total} TK\n")
    print(f"Total {name} price {total} TK")
    grand_total += total
    buy_more = input("You want to buy more? Type 'y' for Yes or 'n' for No: ")
    clear()
    return buy_more


while True:
    choice = start()

    if choice == 'e':
        print(f"Thank you for buying with us.")
        break
    elif choice == "t":
        with open("purchase_history.txt", "a") as file:
            file.write(f"----------------------------\n")
            file.write(f"Grand Total: {grand_total}\nPurchase Time: {current_datetime}")
        print(f"Grand Total: {grand_total}")
        break
    else:
        item_price = items[choice]
        buying_continue = buying(choice, item_price)

        if buying_continue == 'n':
            with open("purchase_history.txt", "a") as file:
                file.write(f"----------------------------\n")
                file.write(f"Grand Total: {grand_total} TK\nPurchase Time: {current_datetime}")
            break
