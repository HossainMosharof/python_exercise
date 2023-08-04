# importing methods
import random
import os

#clearing the terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# Global variable
total_ticket = 10
boy = 0
girl = 0
child = 0

# Creating the list of Audience
audience_type = ["Boy", "Girl", "Child"]

#calculating
def calculation(press):
    global boy, girl, child, total_ticket
    int(input(f"Press {press} for sell the ticket: "))
    if press == 1:
        boy += 1
    elif press == 2:
        girl += 1
    elif press == 3:
        child += 1
    else:
        print(f"Please enter a valid number")
    total_ticket -= 1
    clear()


while total_ticket > 0:
    # Getting random element from list
    audience = random.choice(audience_type)
    print(f"You have only {total_ticket} available ticket left")
    print(f"A {audience} come for ticket")
    if audience == "Boy":
        calculation(1)
    elif audience == "Girl":
        calculation(2)
    elif audience == "Child":
        calculation(3)

redirect = int(input("Press 4 for total invoice: "))
if redirect == 4:
    boy_total = boy * 10
    girl_total = girl * 10
    child_total = child * 5
    print(f"Total ticket sold to boys {boy}*10: {boy_total}")
    print(f"Total ticket sold to girs {girl}*10: {girl_total}")
    print(f"Total ticket sold to child {child}*5: {child_total}")
    print(f"------------------------------------")
    print(f"Grand Total: {boy_total + girl_total + child_total}")
