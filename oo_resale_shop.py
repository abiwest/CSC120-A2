from computer import *

class ResaleShop:

    # What attributes will it need?
    
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, inventory = None):
        if inventory is None:
            inventory = [] # creates an empty list to start
        self.inventory = inventory

    # What methods will you need?
    def buy(self, computer: Computer):
        self.inventory.append(computer)
        return self.inventory.index(computer)
    
    def update_price(self, item_id: int, new_price: int):
        if self.inventory[item_id] is not None:
            self.inventory[item_id].price = new_price
        else:
            print("Item", item_id, "not found. Cannot update price.")

    def refurbish(self, item_id: int, new_os: Optional[str] = None):
        if self.inventory[item_id] is not None:
            computer = self.inventory[item_id]
            computer.refurbish(new_os)  # call the refurbish function from computer
        else:
            print("Item", item_id, "not found. Cannot refurbish.")

    def sell(self, item_id: int):
        if self.item_id is not None:
            self.inventory.pop(item_id)
            print("Item", item_id, "sold!")
        else: 
            print("Item", item_id, "not found. Please select another item to sell.")

    def print_inventory(self):
        # If the inventory is not empty
        if self.inventory:
            # For each item
            for item in self.inventory:
                # Print its details
                print(f'Item ID: {self.inventory.index(item)} : {item}')
        else:
            print("No inventory to display.")


def main():
    shop = ResaleShop() #creates the resale shop

    # creates the new computer for the store
    mac = Computer(description = "2019 MacBook Pro", 
                       processor_type = "Intel", 
                       hard_drive_capacity = 256, 
                       memory = 16, 
                       operating_system = "High Sierra", 
                       year_made = 2019, 
                       price = 1000)
    
    item_id = shop.buy(mac) # add the computer to the inventory

    # shows the inventory
    shop.print_inventory()

    # update the mac OS
    shop.refurbish(item_id, "Monterey")
    # reprint the inventory
    shop.print_inventory()

main()