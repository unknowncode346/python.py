import json

products = {}
cart = {}

def loading_inventory():
   print("You entered 1 for loading inventory.")
   """Load data from a JSON files"""
   try:
       with open('data/inventory.json') as file:
           data = json.load(file)
       return data
   except (FileNotFoundError, json.JSONDecodeError) as e:
       print(f"Error loading data: {e}")
       return {}


def displaying_inventory():
    print("You entered 2 for displaying inventory.")
    print("--------")
    for name, details in products.items():
       print(f"{name} - ${details['price']}")
    print("--------") 


def shopping():
    print("You entered 3 for shopping.")


def displaying_cart():
    print("You entered 4 for displaying cart.")

def quit():
    print("Enter q or Q to quit")

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
