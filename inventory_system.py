"""Inventory management system module."""

import json
from datetime import datetime
import ast


class Inventory:
    """Class representing a simple inventory management system."""

    def __init__(self):
        """Initialize the inventory with empty stock and logs."""
        self.stock_data = {}
        self.logs = None

    def add_item(self, item: str, qty: int):
        """Add an item and quantity to the inventory with validation."""
        if self.logs is None:
            self.logs = []

        if not isinstance(item, str):
            raise TypeError(f"Item name must be a string, got {type(item).__name__}")
        if not isinstance(qty, int):
            raise TypeError(f"Quantity must be an integer, got {type(qty).__name__}")
        if qty <= 0:
            raise ValueError("Quantity must be greater than zero")

        self.stock_data[item] = self.stock_data.get(item, 0) + qty
        log_entry = f"{datetime.now():%Y-%m-%d %H:%M:%S}: Added {qty} of {item}"
        self.logs.append(log_entry)
        print(log_entry)
        return True

    def remove_item(self, item, qty):
        """Remove a quantity of an item from the inventory."""
        try:
            self.stock_data[item] -= qty
            if self.stock_data[item] <= 0:
                del self.stock_data[item]
        except KeyError:
            print(f"Item '{item}' not found in stock.")
        except TypeError:
            print("Invalid quantity type.")
        # except Exception as err:
        #     print(f"Unexpected error: {err}")

    def get_qty(self, item):
        """Return the quantity of a specific item."""
        return self.stock_data.get(item, 0)

    def load_data(self, file="inventory.json"):
        """Load inventory data from a JSON file."""
        with open(file, "r", encoding="utf-8") as f:
            self.stock_data = json.load(f)

    def save_data(self, file="inventory.json"):
        """Save inventory data to a JSON file."""
        with open(file, "w", encoding="utf-8") as f:
            json.dump(self.stock_data, f, indent=4)

    def print_data(self):
        """Print the current inventory."""
        print("Items Report")
        for item, qty in self.stock_data.items():
            print(f"{item} -> {qty}")

    def check_low_items(self, threshold=5):
        """Return a list of items with quantity below a threshold."""
        return [item for item, qty in self.stock_data.items() if qty < threshold]


def main():
    """Main function to demonstrate inventory operations."""
    inv = Inventory()
    try:
        inv.add_item("apple", 10)
        inv.add_item("banana", 2)
        inv.add_item("orange", 1)
        inv.remove_item("apple", 3)
        print("Apple stock:", inv.get_qty("apple"))
        print("Low items:", inv.check_low_items())
        inv.save_data()
        inv.load_data()
        inv.print_data()
    except (TypeError, ValueError) as err:
        print(f"Error: {err}")

    # Safe eval replacement example
    data_str = "{'status': 'ok'}"
    safe_data = ast.literal_eval(data_str)
    print(safe_data)


if __name__ == "__main__":
    main()
