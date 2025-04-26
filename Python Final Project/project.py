import os

inventory = {}

def save_inventory():
    with open("inventory.txt", "w") as file:
        for item, details in inventory.items():
            file.write(f"{item},{details['category']},{details['quantity']},{details['price']}\n")
    print("Inventory saved successfully.")

def load_inventory():
    if os.path.exists("inventory.txt"):
        with open("inventory.txt", "r") as file:
            for line in file:
                name, category, quantity, price = line.strip().split(",")
                inventory[name] = {
                    "category": category,
                    "quantity": int(quantity),
                    "price": float(price)
                }
        print("Inventory loaded successfully.")
    else:
        print("No saved inventory found.")

def add_item(name, category, quantity, price):
    inventory[name] = {
        "category": category,
        "quantity": quantity,
        "price": price
    }
    print(f"Item '{name}' added successfully.")

def remove_item(name):
    if name in inventory:
        del inventory[name]
        print(f"Item '{name}' removed successfully.")
    else:
        print(f"Item '{name}' not found in inventory.")

def update_item(name, quantity=None, price=None):
    if name in inventory:
        if quantity is not None:
            inventory[name]["quantity"] = quantity
        if price is not None:
            inventory[name]["price"] = price
        print(f"Item '{name}' updated successfully.")
    else:
        print(f"Item '{name}' not found in inventory.")

def view_items():
    if inventory:
        print(f"{'Name':<15} {'Category':<12} {'Quantity':<10} {'Price':<10}")
        print("-" * 50)
        for item, details in inventory.items():
            print(f"{item:<15} {details['category']:<12} {details['quantity']:<10} {details['price']:<10.2f}")
    else:
        print("Inventory is empty.")

def search_items(query):
    found = False
    for item, details in inventory.items():
        if query.lower() in item.lower() or query.lower() in details["category"].lower():
            found = True
            print(f"Name: {item}, Category: {details['category']}, Quantity: {details['quantity']}, Price: {details['price']}")
    if not found:
        print(f"No items found for '{query}'.")

def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def main_menu():
    load_inventory()  # Load inventory on startup
    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Update Item")
        print("4. View All Items")
        print("5. Search Items")
        print("6. Save Inventory")
        print("7. Load Inventory")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter item name: ")
            category = input("Enter category: ")
            quantity = get_positive_integer("Enter quantity: ")
            price = get_positive_float("Enter price: ")
            add_item(name, category, quantity, price)

        elif choice == "2":
            name = input("Enter item name to remove: ")
            remove_item(name)

        elif choice == "3":
            name = input("Enter item name to update: ")
            quantity = input("Enter new quantity (press Enter to skip): ")
            price = input("Enter new price (press Enter to skip): ")

            quantity = int(quantity) if quantity else None
            price = float(price) if price else None

            update_item(name, quantity, price)

        elif choice == "4":
            view_items()

        elif choice == "5":
            query = input("Enter item name or category to search: ")
            search_items(query)

        elif choice == "6":
            save_inventory()

        elif choice == "7":
            load_inventory()

        elif choice == "8":
            save_inventory()
            print("Exiting the program...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()
