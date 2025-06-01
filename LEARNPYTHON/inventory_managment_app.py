# Simple Inventory Management Program

# https://github.com/DANIEL-CHRISTIAN-KIZITO/Kizito_Daniel_Junior.git

# Initial inventory (item: quantity)
inventory = {
    "Dresses": 10,
    "Trausers": 25,
    "Shirts": 15
}

while True:
    print("\nInventory Management System")
    print("1. View Inventory")
    print("2. Update Stock")
    print("3. Exit")
    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        print("\nCurrent Inventory:")
        for item, quantity in inventory.items():
            print(f"{item}: {quantity}")

    elif choice == "2":
        item_name = input("Enter item name to update: ")
        if item_name in inventory:
            try:
                amount = int(input("Enter new quantity: "))
                inventory[item_name] = amount
                print(f"{item_name} updated to {amount}.")
            except ValueError:
                print("Please enter a valid number.")
        else:
            print("Item not found in inventory.")

    elif choice == "3":
        print("Exiting Inventory Management System.")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
