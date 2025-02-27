from typing import Dict, Union

from procedural_resale_shop import buy, update_price, sell, print_inventory, refurbish

# Attributes
def create_computer(description: str,
                    processor_type: str,
                    hard_drive_capacity: int,
                    memory: int,
                    operating_system: str,
                    year_made: int,
                    price: int):
    return {'description': description,
            'processor_type': processor_type,
            'hard_drive_capacity': hard_drive_capacity,
            'memory': memory,
            'operating_system': operating_system,
            'year_made': year_made,
            'price': price
    }

def main():
    

    computer = create_computer(
        "Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500
    )

    print("-" * 21)
    print("COMPUTER RESALE STORE")
    print("-" * 21)

    print("Buying", computer["description"])
    print("Adding to inventory...")
    computer_id = buy(computer)
    print("Done.\n")

    print("Checking inventory...")
    print_inventory()
    print("Done.\n")

    new_OS = "MacOS Monterey"
    print("Refurbishing Item ID:", computer_id, ", updating OS to", new_OS)
    print("Updating inventory...")
    refurbish(computer_id, new_OS)
    print("Done.\n")

    print("Checking inventory...")
    print_inventory()
    print("Done.\n")
    
    print("Selling Item ID:", computer_id)
    sell(computer_id)
    
    print("Checking inventory...")
    print_inventory()
    print("Done.\n")

if __name__ == "__main__": main()
