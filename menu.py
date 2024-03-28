# Create an empty list to store customer orders
customer_orders = []

# Example of adding orders to the list
[
    {
    "Item name": "Apple",
    "Price": 1.25,
    "Quantity": 3
},

{
    "Item name": "Banana",
    "Price": 0.75,
    "Quantity": 2
    },
]

# Adding orders to the list
customer_orders.append(order1)
customer_orders.append(order2)



# Initializations
place_order = True

while True:
    # Printing the sub-menu
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
   
