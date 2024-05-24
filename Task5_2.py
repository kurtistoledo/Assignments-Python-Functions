# Lesson 5: Python Functions
# 2. The Shopping List Maker

class ShoppingList:
    def __init__(self):
        self.items = {}  # Initialize an empty dictionary to store items

    def add_item(self, item, price):
        self.items[item] = price  # Add an item with its price to the list

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]  # Remove the specified item
        else:
            print(f"{item} is not in the shopping list.")

    def print_list(self):
        print("Shopping List:")
        for item, price in self.items.items():
            print(f"{item}: ${price:.2f} per unit")

# Example usage
my_list = ShoppingList()
my_list.add_item("Apples", 2.99)
my_list.add_item("Milk", 1.49)
my_list.add_item("Bread", 3.25)

my_list.print_list()

# Remove an item
my_list.remove_item("Milk")
my_list.print_list()
