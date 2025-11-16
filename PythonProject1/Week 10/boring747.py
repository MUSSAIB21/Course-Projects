# Inventory will be a list of dictionaries
inventory = []

# Load inventory from a text file
def load_inventory():
    global inventory
    inventory = []
    try:
        file = open("inventory.txt", "r")
        for line in file:
            line = line.strip()
            if line:
                id_, name, category, price, quantity = line.split(",")
                inventory.append({
                    "id": id_,
                    "name": name,
                    "category": category,
                    "price": float(price),
                    "quantity": int(quantity)
                })
        file.close()
        print("Inventory loaded!")
    except:
        print("No file found or error reading file. Starting fresh!")

# Save inventory to a text file
def save_inventory():
    file = open("inventory.txt", "w")
    for part in inventory:
        line = f"{part['id']},{part['name']},{part['category']},{part['price']},{part['quantity']}\n"
        file.write(line)
    file.close()
    print("Inventory saved!")

# Get a valid number input
def get_number(prompt, number_type=float):
    while True:
        value = input(prompt)
        try:
            return number_type(value)
        except:
            print("Invalid input! Please enter a valid number.")

# Add a new part
def add_part():
    part = {}
    part["id"] = input("Enter part ID: ")
    part["name"] = input("Enter part name: ")
    part["category"] = input("Enter category (engine, brakes, etc.): ")
    part["price"] = get_number("Enter price: ", float)
    part["quantity"] = get_number("Enter quantity: ", int)
    part["inStock"] = False
    if part["quantity"] > 0:
        part["inStock"] = True

    inventory.append(part)
    print("Part added!")

# Delete part by ID
def delete_part():
    part_id = input("Enter part ID to delete: ")
    for part in inventory:
        if part["id"] == part_id:
            inventory.remove(part)
            print("Part deleted.")
            return
    print("Part not found.")

# Search by name
def search_part():
    name = input("Enter name to search: ").lower()
    found = False
    for part in inventory:
        if name in part["name"].lower():
            print(part)
            found = True
    if not found:
        print("No part found with that name.")

# Update a part
def update_part():
    part_id = input("Enter part ID to update: ")
    for part in inventory:
        if part["id"] == part_id:
            print("Leave blank to keep current value.")
            new_name = input("Enter new name: ")
            if new_name:
                part["name"] = new_name
            new_cat = input("Enter new category: ")
            if new_cat:
                part["category"] = new_cat
            price_input = input("Enter new price: ")
            if price_input:
                try:
                    part["price"] = float(price_input)
                except:
                    print("Invalid price. Keeping old value.")
            quantity_input = input("Enter new quantity: ")
            if quantity_input:
                try:
                    part["quantity"] = int(quantity_input)
                except:
                    print("Invalid quantity. Keeping old value.")
            print("Part updated!")
            return
    print("Part ID not found.")

# View all parts
def view_all_parts():
    global inventory
    if not inventory:
        print("No parts in inventory.")
    else:
        inventory = sorted(inventory, key=lambda k: k["id"])
        for part in inventory:
            print(part)

# Main menu loop
def menu():
    load_inventory()
    while True:
        print("\n--- Car Parts Inventory ---")
        print("1. Add Part")
        print("2. Delete Part")
        print("3. Search Part")
        print("4. Update Part")
        print("5. View All Parts")
        print("6. Save Inventory")
        print("7. Load Inventory")
        print("8. Exit")

        choice = input("Choose an option (1-8): ")
        if choice == "1":
            add_part()
        elif choice == "2":
            delete_part()
        elif choice == "3":
            search_part()
        elif choice == "4":
            update_part()
        elif choice == "5":
            view_all_parts()
        elif choice == "6":
            save_inventory()
        elif choice == "7":
            load_inventory()
        elif choice == "8":
            print("Goodbye, road warrior!")
            break
        else:
            print("Not a valid choice! Please try again.")

# Start the menu
menu()