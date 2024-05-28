# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
order_list=[]

# Launch the store and present a greeting to the customer
print("=" * 41)
print("|  Welcome to DC's variety food truck.  |")
print("=" * 41)
# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    
    # Ask the customer from which menu category they want to order
    print("\nWhich menu would you like to order from? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

        # Get the customer's input
    select_menu=True
    while select_menu==True:    
        menu_category = input("Type menu number: ")

        # Check if the customer's input is a number
        if menu_category.isdigit():
            # Check if the customer's input is a valid option
            if int(menu_category) in menu_items.keys():
                # Save the menu category name to a variable
                menu_category_name = menu_items[int(menu_category)]
                # Print out the menu category name they selected
                print(f"\nYou selected {menu_category_name}")

                # Print out the menu options from the menu_category_name
                print(f"What {menu_category_name} item would you like to order?")
                i = 1
                menu_items = {}
                print("------------------------------------------")
                print("Item # | Item name                | Price")
                print("-------|--------------------------|-------")
                for key, value in menu[menu_category_name].items():
                    # Check if the menu item is a dictionary to handle differently
                    if type(value) is dict:
                        for key2, value2 in value.items():
                            num_item_spaces = 24 - len(key + key2) - 3
                            item_spaces = " " * num_item_spaces
                            print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                            menu_items[i] = {
                                "Item name": key + " - " + key2,
                                "Price": value2
                            }
                            i += 1
                    else:
                        num_item_spaces = 24 - len(key)
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key}{item_spaces} | ${value}")
                        menu_items[i] = {
                            "Item name": key,
                            "Price": value
                        }
                        i += 1
                print("------------------------------------------\n")
                # 2. Ask customer to input menu item number
                place_order_item=True

                while place_order_item:
                    menu_selection=input("Please select a menu item from the list: ")

                    # 3. Check if the customer typed a number
                    if menu_selection.isdigit():
                    # Convert the menu selection to an integer
                        menu_selection=int(menu_selection)

                        # 4. Check if the menu selection is in the menu items
                        if menu_selection in menu_items.keys():
                            
                            # Store the item name as a variable
                            menu_selection_item=menu_items[menu_selection]["Item name"]
                            menu_selection_price=menu_items[menu_selection]["Price"]
                            
                            # Ask the customer for the quantity of the menu item
                            quantity=input(f"How many {menu_selection_item}s would you like? (Default 1): ")

                            # Check if the quantity is a number, default to 1 if not
                            if quantity.isdigit():
                                quantity=int(quantity)
                                if quantity<1:
                                    quantity=1
                            else:
                                quantity=1

                            # Add the item name, price, and quantity to the order list                    
                            
                            order_list.append({"Item name":menu_selection_item, "Price":menu_selection_price, "Quantity":quantity})
                            place_order_item=False
                            select_menu=False
                        else:
                            # Tell the customer that their input isn't valid
                            print(f"{menu_selection} was not a menu option.")
                    # Tell the customer they didn't select a menu option
                    else:
                        print(f"You didn't select a number from the {menu_category_name} menu.")
            else:
                # Tell the customer they didn't select a menu option
                print(f"{menu_category} was not a menu option.")
        else:
            # Tell the customer they didn't select a number
            print("You didn't select a number.")

    while True:
        # Ask the customer if they would like to order anything else
        keep_ordering = input("\nWould you like to keep ordering? (Y)es or (N)o ")

        # 5. Check the customer's input
        match keep_ordering.upper():
            # Keep ordering
            case "Y":
                break
            case "N":
                # Exit the keep ordering question loop
                place_order=False
                break
            # Tell the customer to try again
            case _:
                "Invalid selection. Please make a valid selection."
        
# Complete the order

# Since the customer decided to stop ordering, thank them for
# their order
print("\n\nThank you for your order!")
print("This is what we are preparing for you.\n")

# Uncomment the following line to check the structure of the order
#print(order)

# Print out the customer's order
print("-" * 56)
print("Item name                 | Price  | Quantity |  Total  ")
print("--------------------------|--------|----------|---------")

# 6. Calculate the cost of the order using list comprehension
# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.

item_total_list = [item["Price"]*item["Quantity"] for item in order_list]
item_total = sum(item_total_list)
item_total = f"${item_total:,.2f}"

# 7. Loop through the items in the customer's order

i=0
for orders in order_list:

    # 8. Store the dictionary items as variables
    order_item=orders['Item name']
    order_price=f"${orders['Price']:,.2f}"
    order_quantity=orders['Quantity']
    order_line_total=f"${item_total_list[i]:,.2f}"
    
    # 9. Calculate the number of spaces for formatted printing
    order_item_spaces_cnt=(26 - len(orders['Item name']))
    order_price_spaces_cnt=(6 - len(str(orders['Price'])))
    order_quantity_spaces_cnt=(9 - len(str(orders['Quantity'])))
    order_line_total_spaces_cnt=(9-len(order_line_total))

    # 10. Create space strings
    order_item_spaces = " " * order_item_spaces_cnt
    order_price_spaces = " " * order_price_spaces_cnt
    order_quantity_spaces = " " * order_quantity_spaces_cnt
    order_line_total_spaces = " " * order_line_total_spaces_cnt

    # 11. Print the item name, price, quantity and item totals
    print(f"{order_item}{order_item_spaces}| {order_price}{order_price_spaces}| {order_quantity}{order_quantity_spaces}|{order_line_total_spaces}{order_line_total}")

    i += 1
print("=" * 56)

len_item_total = len(item_total)
item_total_spaces=" " * (45-len_item_total)
print(f"Grand Total{item_total_spaces}{item_total}")
print("=" * 56)