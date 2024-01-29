#  Create three dictionaries to store customer, product and order information.
CustomersDatabase = {}
ProductsDatabase = {}
orders = {}

def add_customer(customer_id, name, contact_details):
    # Add a new customer to the database
    if customer_id in CustomersDatabase:
        print("User id already exists, please change it and try again!")
    else:
        CustomersDatabase[customer_id] = {
        "name": name,
        "contact_details": contact_details,
        "order_history": []
    }
        print(f"Customer {name} added successfully!")

def remove_customer(customer_id):
    # Remove a customer from the database
    if customer_id in CustomersDatabase:
        del CustomersDatabase[customer_id]
        print("Customer removed successfully.")
    else:
        print("Customer not found.")

def display_customer_details(customer_id):
    # Search for customer information by id
    if customer_id in CustomersDatabase:
        customer = CustomersDatabase[customer_id]
        print("\nCustomer Details are following:")
        print(f"Customer ID: {customer_id}")
        print(f"Name: {customer['name']}")
        print(f"Contact Details: {customer['contact_details']}")
        print("Order History:")
        for order in customer['order_history']:
            print(f"  - Order ID: {order['order_id']}, Total Cost: ${order['total_cost']}")
    else:
        print("Customer not found.")

def add_product(product_name, price, quantity):
    # Add a new product to the database
    if product_name in ProductsDatabase:
        ProductsDatabase[product_name] += price
        ProductsDatabase[product_name] += quantity
    else:
        ProductsDatabase[product_name] = price
        ProductsDatabase[product_name] = quantity
    print(f"Added {quantity} {product_name}(s).")

def view_inventory():
    for product_name, price, quantity in ProductsDatabase.items():
        print(f"{product_name}: {quantity},{price}$")

def update_product_quantity(product_name, quantity):
    # Update product information
    if product_name in ProductsDatabase:
        ProductsDatabase[product_name] = quantity
        print(f"Updated {product_name} quantity to {quantity}.")
    else:
        print("Product not found.")

def add_product_to_order(customer_id, product_name, quantity):
    if customer_id in CustomersDatabase and product_name in ProductsDatabase:
        product = ProductsDatabase[product_name]
        total_cost = product["price"] * quantity

        if update_product_quantity(product_name, quantity):
            order_id = len(orders) + 1
            order = {"order_id": order_id, "product_name": product_name, "quantity": quantity, "total_cost": total_cost}
            CustomersDatabase[customer_id]["order_history"].append(order)
            orders[order_id] = order
            print(f"Product added to order. Order ID: {order_id}, Total Cost: ${total_cost}")
    else:
        print("Customer or product not found.")

def calculate_total_sales():
    # Calculate total sales
    total_sales = sum(order["total_cost"] for order in orders.values())
    print(f"Total Sales: ${total_sales}")

def display_most_popular_products():
    # Calculate the most popular products based on product sales
    if orders:
        product_sales = {}
        for order in orders.values():
            product_id = order["product_id"]
            product_sales[product_id] = product_sales.get(product_id, 0) + order["quantity"]

        most_popular_product_id = max(product_sales, key=product_sales.get)
        most_popular_product_name = ProductsDatabase[most_popular_product_id]["name"]
        print(f"Most Popular Product: {most_popular_product_name}")
    else:
        print("No orders placed yet.")
        
# Test cases



def CustomerOrderManagementSystem():
    while True:
        print("\nWelcome to Customer Order Management System")
        print("1. Customer Management")
        print("2. Product Management")
        print("3. Order Management")
        print("4. View Total Sales")
        print("5. View Most Popular Products")
        print("6. Exit")
        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '1':
            print("\nWelcome to Customer Management System")
            print("1. Add Customer")
            print("2. Remove Customer")
            print("3. Search for customer details")
            print("4. Return to upper menu")
            choice_1 = input("Enter choice (1/2/3/4/5): ")

            if choice_1 == '1':
                customer_id = input("Create Customer ID: ")
                name = input("Enter Customer name: ")
                contact_details = input("Enter Customer E-mail: ")
                add_customer(customer_id,name,contact_details)
            elif choice_1 =='2':
                customer_id = input("Enter Customer ID: ")
                remove_customer(customer_id)
            elif choice_1 =='3':
                customer_id = input("Enter Customer ID: ")
                display_customer_details(customer_id)
            elif choice_1 == '4':
                CustomerOrderManagementSystem()
            else:
                print("Invalid choice. Please choose again.")

        elif choice == '2':
            print("\nWelcome to Product Management System")
            print("1. Add Product")
            print("2. View Inventory")
            print("3. Update Product Quantity")
            print("4. Return to upper menu")
            choice_2 = input("Enter choice (1/2/3/4/5): ")

            if choice_2 == '1':
                product_name = input("Enter item name: ")
                price = input("Enter item price: ")
                quantity = int(input("Enter quantity: "))
                add_product(product_name,price,quantity)
            elif choice_2 =='2':
                view_inventory()
            elif choice_2 =='3':
                product_name = input("Enter item name: ")
                quantity = int(input("Enter new quantity: "))
                update_product_quantity(product_name, quantity)
            elif choice_2 == '4':
                CustomerOrderManagementSystem()
            else:
                print("Invalid choice. Please choose again.")

        elif choice == '3':
            print("\nWelcome to Order Management System")
            customer_id = input("Enter Customer ID: ")
            product_name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            add_product_to_order(customer_id, product_name, quantity)
        elif choice == '4':
            calculate_total_sales()
        elif choice == '5':
            display_most_popular_products()
        elif choice == '6':
            print("Exiting Inventory Management System.")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    CustomerOrderManagementSystem()
