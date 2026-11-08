import json

products = {}
cart = {}

def loading_inventory():
   """Load data from a JSON files"""
   try:
    with open('data/inventory.json') as file:
     data = json.load(file)
    print()
    print("------------------------------------------")
    print(" Inventory successfully loaded!")
    print("------------------------------------------")
    print() 
    return data
   except (FileNotFoundError, json.JSONDecodeError) as e:
    print(f"Error loading data: {e}")
    return {}


def displaying_inventory():
    print("")
    print("You entered 2 for displaying inventory.")
    print("--------")
    for name, details in products.items():
        print(f"{name} - ${details['price']}")
        print("--------")


def displaying_item(cart_item):
    print("")
    print("----------------------------------")
    print(f"{cart_item['name']} - ${cart_item['price']}")
    print("----------------------------------")  
    for item in cart:
       print(f"{item['name']} - ${item['price']}")



def shopping():
    print("--------")
    print("Please start scanning your first item. Type 'done' when you are finished.")
    print("Hit Enter key to STOP scaning")

while True:
    print("---------------------------------")
    print("Enter 1 for loading inventory:")
    print("Enter 2 for displaying inventory:")
    print("Enter 3 for shopping:")
    print("Enter 4 for displaying cart:")
    print("Enter q or Q to quit")
    print("---------------------------------")

    barcode = input("Enter your choice: ")

    menu_option= input ("Please enter your option here: ")
    if menu_option == "1":
        products = loading_inventory()
        print("You entered 1 for loading inventory.")

    elif menu_option == "2":
        displaying_inventory()

    elif menu_option == "3":
        shopping() 
    elif menu_option == "4":
        cart() 
    elif menu_option == "q" or menu_option == "Q":
        print("Good Bye")
        break
    else:
     print("Invalid option, please try again!")
                     

def quit():
    print("Goodbye!")


