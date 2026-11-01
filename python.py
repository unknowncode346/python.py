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
        # At the start match= False will be set to True once item is found in the inventory
        match = False
        item = input("Please scan your item: ")
        if item.lower() == "done":
            break
        for name, details in products.items():
            if item.lower() == name.lower():
                match = True
                quantity = input(f"How many {name} would you like to add to your cart? ")
                if quantity.isdigit() and int(quantity) > 0:
                    cart[name] = cart.get(name, 0) + int(quantity)
                    print(f"{quantity} {name}(s) added to your cart.")
                else:
                    print("Invalid quantity. Please enter a positive integer.")
                break
        if not match:
            print(f"{item} is not found in the inventory. Please try again.")




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
    elif menu_option == "3":
        print("You entered option 3 for shopping")
    elif menu_option == "4":
        print("You entered option 4 for displaying cart")
    elif menu_option == "q" or menu_option == "Q":
        print("Goodbye!")
        break

    else:
        print("You entered an invalid option please try again.")
