import json

products = {}
cart = {}

def loading_inventory():
   """Load data from a JSON files"""
   try:
       with open('data/inventory.json') as file:
           data = json.load(file)
       return data
   except (FileNotFoundError, json.JSONDecodeError) as e:
       print(f"Error loading data: {e}")
       return {}


def displaying_inventory():
    print("--------")
    for name, details in products.items():
       print(f"{name} - ${details['price']}")
    print("--------") 


def shopping():
    print("--------")
    print("Please start scanning your first item. Type 'done' when you are finished.")
    print("Hit Enter key to STOP scaning")
    while True:
        barcode = input("Scan your item: ")
        if barcode == "#":  
            print("Enter item barcode")

def displaying_cart():
    print("--------")
    for name, quantity in cart.items():
        print(f"{name} - Quantity: {quantity}")
    print("--------")

def quit():
    print("Goodbye!")

while True:
    print("----------------------------------------")
    print("Enter 1 for loading inventory:")
    print("Enter 2 for displaying invetory:")
    print("Enter 3 for shopping:")
    print("Enter 4 for displaying cart:")
    print("Enter q or Q to quit")
    print("----------------------------------------")

    menu_option= input ("Please enter your option here: ")
    print("You entered option: " + menu_option)

    if menu_option == "1":
        print("You entered option 1 for loading inventory")
        products = loading_inventory()
    elif menu_option == "2":   
        print("You entered option 2 for displaying inventory")
        displaying_inventory()
    elif menu_option == "3":
        print("You entered option 3 for shopping")
        shopping()
    elif menu_option == "4":
        print("You entered option 4 for displaying cart")
        displaying_cart()
    elif menu_option == "q" or menu_option == "Q":
        print("Goodbye!")
        break

    else:
        print("You entered an invalid option please try again.")
