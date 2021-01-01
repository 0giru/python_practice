MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

import sys

global WATER
global MILK
global COFFEE
global MONEY
global ORDER
global CHECK

WATER = 500
MILK = 600
COFFEE = 120
MONEY = 0
ORDER = ""
CHECK = False

# TODO : 1. Prompt user by asking "What would you like?"
def check_order():
    global ORDER
    ORDER = input("What would you like? : ")

# TODO : 2. Turn Off Coffee Machine by entering "OFF" to the prompt
def off_machine():
    sys.exit()

# TODO : 3. print all of resources of machine
def print_resources():
    global WATER
    global MILK
    global COFFEE
    global MONEY
    global ORDER
    print(f"WATER : {WATER}ml\n")
    print(f"MILK : {MILK}ml\n")
    print(f"COFFEE : {COFFEE}g\n")
    print(f"MONEY : ${MONEY}\n")

def insert_cal_money():
    global CHECK
    global ORDER
    global MONEY
    global WATER
    global MILK
    global COFFEE
    temp_quarters = 0
    temp_dimes = 0
    temp_nickles = 0
    temp_pennies = 0

    temp_quarters = input("how many quarters? : \n")
    temp_dimes = input("how many dimes? : \n")
    temp_nickles = input("how many nickles? : \n")
    temp_pennies = input("how many pennies? : \n")

    temp_total = float(temp_dimes) * 0.10 + float(temp_nickles) * 0.05 + float(temp_pennies) * 0.01 + float(temp_quarters) * 0.25

    if ORDER == "espresso":
        if temp_total >= 1.5:
            MONEY += 1.5
            WATER = WATER - 50
            COFFEE = COFFEE - 18
            change = temp_total - 1.5
            print("Here is $" + str(round(change, 2)) + "dollars in change")
        elif temp_total < 1.5:
            print("Sorry, not enough money, Money Refunded")
            MONEY = MONEY

    elif ORDER == "latte":
        if temp_total >= 2.5:
            MONEY += 2.5
            WATER = WATER - 200
            COFFEE = COFFEE - 24
            MILK = MILK - 150
            change = temp_total - 2.5
            print("Here is $" + str(round(change, 2)) + "dollars in change")
        elif temp_total < 2.5:
            print("Sorry, not enough money, Money Refunded")
            MONEY = MONEY

    elif ORDER == "cappuccino":
        if temp_total >= 3:
            MONEY += 3
            WATER = WATER - 300
            COFFEE = COFFEE - 100
            MILK = MILK - 200
            change = temp_total - 3
            print("Here is $" + str(round(change, 2)) + "dollars in change")
        elif temp_total < 3:
            print("Sorry, not enough money, Money Refunded")
            MONEY = MONEY

while True:
    check_order()
    if ORDER == "off":
        # print("turn off machine")
        off_machine()
    elif ORDER == "report":
        print_resources()
        continue
    else:
        if ORDER == "espresso":
            if (WATER >= 50) and (COFFEE >= 18):
                CHECK = True
            elif WATER < 50:
                print("Sorry, Not enough Water")
                continue
            elif COFFEE < 18:
                print("Sorry, Not enough Coffee")
                continue
            elif (WATER < 50) and (COFFEE < 18):
                print("Sorry, Not enough Water And Coffee")
                continue
        elif ORDER == "latte":
            if (WATER >= 200) and (COFFEE >= 24) and (MILK >= 150):
                CHECK = True
            elif WATER < 200:
                print("Sorry, Not enough Water")
                continue
            elif COFFEE < 24:
                print("Sorry, Not enough Coffee")
                continue
            elif MILK < 150:
                print("Sorry, Not enough Milk")
                continue
            elif (WATER < 200) and (COFFEE < 24):
                print("Sorry, Not enough Water And Coffee")
                continue
            elif (WATER < 200) and (MILK < 150):
                print("Sorry, Not enough Water And Milk")
                continue
            elif (COFFEE < 24) and (MILK < 150):
                print("Sorry, Not enough Water And Coffee")
                continue
            elif (COFFEE < 24) and (MILK < 150) and (WATER < 200):
                print("Sorry, Not enough Water And Coffee And Milk")
                continue
        elif ORDER == "cappuccino":
            if (WATER >= 300) and (COFFEE >= 100) and (MILK >= 200):
                CHECK = True
            elif WATER < 300:
                print("Sorry, Not enough Water")
                continue
            elif COFFEE < 100:
                print("Sorry, Not enough Coffee")
                continue
            elif MILK < 200:
                print("Sorry, Not enough Milk")
                continue
            elif (WATER < 300) and (COFFEE < 100):
                print("Sorry, Not enough Water And Coffee")
                continue
            elif (WATER < 300) and (MILK < 200):
                print("Sorry, Not enough Water And Milk")
                continue
            elif (COFFEE < 100) and (MILK < 200):
                print("Sorry, Not enough Water And Coffee")
                continue
            elif (COFFEE < 100) and (MILK < 200) and (WATER < 300):
                print("Sorry, Not enough Water And Coffee And Milk")
                continue
    if CHECK == True:
        insert_cal_money()