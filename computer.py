from typing import Dict, Optional

class Computer:

    # Attributes
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int

    # Constructor
    def __init__(self, description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price


    """
    Updates the price of the computer based on its age
    Parameters:
    - new_os (Optional[str]): can optionally update the operating system
    """
    def refurbish(self, new_os: Optional[str] = None):
        if self.year_made < 2000:
            self.price = 0
        elif self.year_made < 2012:
            self.price = 250
        elif self.year_made < 2018:
            self.price = 550
        else:
            self.price = 1000

        if new_os is not None:
            self.operating_system = new_os
    
    """
    returns: string of information about the computer
    """
    def __str__(self): # this returns the info about the computer
        return (
            f"Description: {self.description}, Processor: {self.processor_type}, "
            f"Storage: {self.hard_drive_capacity}, Memory: {self.memory}, "
            f"OS: {self.operating_system}, Year: {self.year_made}, Price: {self.price}"
        )