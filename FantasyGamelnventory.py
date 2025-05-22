print("Varun Bellad, 1AY24AI096, Sec-O")
# FantasyGameInventory.py

def display_inventory(inventory):
    print("Inventory:")
    item_total = 0
    for item, count in inventory.items():
        print(f"{count} {item}")
        item_total += count
    print(f"Total number of items: {item_total}")

def add_to_inventory(inventory, added_items):
    for item in added_items:
        inventory[item] = inventory.get(item, 0) + 1
    return inventory

def main():
    # Starting inventory
    inventory = {
        'rope': 1,
        'torch': 6,
        'gold coin': 42,
        'dagger': 1,
        'arrow': 12
    }

    # Loot from a dragon
    dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

    inventory = add_to_inventory(inventory, dragon_loot)
    display_inventory(inventory)

if __name__ == "__main__":
    main()
