inventory = []
def add_item(item):
    inventory.append(item)
def remove_item(item):
    if item in inventory:
        inventory.remove(item)
    else:
        print("You do not have this item in your inventory.")
def show_inventory():
    print(inventory)
while True:
    add = input("What item do you want to add to the inventory list? ")
    add_item(add)
    add_again = input("Do you want to add another item to your inventory list? Write 'yes' or 'no': ")
    if add_again != "yes":
        break
while True:
    remove = input("Do you want to remove an item from your inventory list? Write 'yes' or 'no': ")
    if remove == "yes":
        item_to_remove = input("What item do you want to remove from the inventory list? ")
        remove_item(item_to_remove)
    else:
        print(f"This is your final inventory list: {inventory}!")
        break

