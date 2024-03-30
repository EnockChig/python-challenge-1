# Create an empty list to store customer orders
customer_orders = []

# Create the sub menu and save as empty list
menu_selection = [
    {
    "Item name": "string",
    "Price": float,
    "Quantity": int
    },

    {
    "Item name": "string",
    "Price": float,
    "Quantity": int
    },
]

print (menu_selection)


# Create a tuple containing the names of menu_items:
# snacks, meals, drinks, and dessert.
menu_items = ("snacks", "meals", "drinks", "dessert")

#Create a list of the menu items

snacks = ["chips", "cookies", "nuts", "jerky"]
meals = ["pasta", "jambalaya", "burgers", "steak"]
drinks = ["juice", "wine", "water", "beer"]
dessert = ["ice cream", "yogurt", "cake", "jelly"]

print (menu_items)

# Create a list of item prices
item_prices = [{"snacks": 

# Prompt customer to enter their selection from the menu saving it as variable menu_selection
customer_orders.append(menu_selection)

# Initializations
place_order = True

while True:
    # Printing the customer order
    for num, item in menu_items.items():
        print(f"{num}: {item['Item name']} - ${item['Price']}")

    # Prompting the customer to enter their selection
    menu_selection = input("Please enter the number of your selection from the menu: ")

    # Input validation to check if menu_selection is a number and if it corresponds to a menu item
    if not menu_selection.isdigit():
        print("Error: Invalid input. Please enter a number.")
        continue
    
    menu_selection = int(menu_selection)
    if menu_selection not in menu_items:
        print("Error: Selection not found in the menu.")
        continue
    
    # Get the item name from the menu_items dictionary and store it as a variable
    item_name = menu_items[menu_selection]["Item name"]
    
    # Ask the customer for the quantity of the menu item
    quantity = input(f"How many {item_name}s would you like to order? (Quantity will default to 1 if invalid input): ")
    
    # Check if the customer input for quantity is a number
    if not quantity.isdigit():
        print("Invalid input. Quantity set to 1.")
        quantity = 1
    else:
        # Convert the quantity to an integer
        quantity = int(quantity)
    
    # Append the customer's order to the order list in dictionary format
    order = {
        "Item name": item_name,
        "Price": menu_items[menu_selection]["Price"],
        "Quantity": quantity
    }
    customer_orders.append(order)

    # Asking if the customer wants to continue ordering
    choice = input("Would you like to continue ordering? (y/n): ")

    # Using match-case statement to handle different choices
    match choice.lower():
        case 'y':
            place_order = True
            break
        case 'n':
            place_order = False
            print("Thank you for your order.")
            break
        case _:
            print("Invalid input. Please try again.")

         # Assuming you have the customer_orders list containing dictionaries of orders

     # Loop through the order list
for order in customer_orders:
     print("Item:", order["Item name"])
     print("Price:", order["Price"])
     print("Quantity:", order["Quantity"])
     print("-------------")
   
