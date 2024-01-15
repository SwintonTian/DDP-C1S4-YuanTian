inventory = {"iPhone":1,
             "iPad":2,
             "MacBook":3}

def add_item(item, quantity):
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity

def view_inventory():
    print("\nInventory:")
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")

def update_item(item, quantity):
    if item in inventory:
        inventory[item] = quantity
    else:
        print(f"Item '{item}' not found in the inventory.")

def manage_inventory():
    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. View Inventory")
        print("3. Update Item Quantity")
        print("4. Exit")
        choice = input("Enter choice (1/2/3/4): ")

        if choice == '1':
            item = input("Enter item: ")
            quantity = int(input("Enter quantity: "))
            add_item(item, quantity)
            print(f"Item '{item}' added to the inventory.")
        elif choice == '2':
            view_inventory()
        elif choice == '3':
            item = input("Enter item: ")
            quantity = int(input("Enter new quantity: "))
            update_item(item, quantity)
        elif choice == '4':
            print("Exiting Inventory Management System.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
manage_inventory()
