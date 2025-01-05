class Stack:
    def __init__(self):
        self.stack = []  # List to store stack elements

    # Add an item to the stack (Push)
    def push(self, item):
        self.stack.append(item)
        print(f"Item added to stack: {item}")

    # Remove and return the most recent item from the stack (Pop)
    def pop(self):
        if not self.is_empty():
            item = self.stack.pop()
            print(f"Item removed from stack: {item}")
            return item
        else:
            print("Stack is empty. No items to remove.")
            return None

    # View the most recent item without removing it (Peek)
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty.")
            return None

    # Check if the stack is empty
    def is_empty(self):
        return len(self.stack) == 0

    # Display all items in the stack
    def display(self):
        if not self.is_empty():
            print("Current Stack:")
            for item in reversed(self.stack):
                print(item)
        else:
            print("Stack is empty.")

# Warehouse inventory update using Stack
class WarehouseInventory:
    def __init__(self, capacity):
        self.capacity = capacity  # Maximum number of products allowed
        self.products = {}  # Dictionary to store product details
        self.order_stack = Stack()  # Stack to track inventory updates

    # Add a new product to the inventory
    def add_product(self, product_id, product_name, quantity, priority):
        if len(self.products) >= self.capacity:
            print("Warehouse is full. Cannot add more products.")
            return

        self.products[product_id] = {
            "product_name": product_name,
            "quantity": quantity,
            "priority": priority
        }
        # Record the addition in the stack
        self.order_stack.push(f"Added Product: {product_name} (ID: {product_id})")

    # Update product quantity
    def update_quantity(self, product_id, quantity):
        if product_id in self.products:
            old_quantity = self.products[product_id]["quantity"]
            self.products[product_id]["quantity"] = quantity
            # Record the update in the stack
            self.order_stack.push(f"Updated Product ID {product_id}: Quantity {old_quantity} -> {quantity}")
        else:
            print(f"Product ID {product_id} not found in inventory.")

    # Remove a product from the inventory
    def remove_product(self, product_id):
        if product_id in self.products:
            product_name = self.products[product_id]["product_name"]
            del self.products[product_id]
            # Record the removal in the stack
            self.order_stack.push(f"Removed Product: {product_name} (ID: {product_id})")
        else:
            print(f"Product ID {product_id} not found in inventory.")

    # Display all products in the inventory
    def display_inventory(self):
        if self.products:
            print("Current Inventory:")
            for product_id, details in self.products.items():
                print(f"ID: {product_id}, Name: {details['product_name']}, "
                      f"Quantity: {details['quantity']}, Priority: {details['priority']}")
        else:
            print("Inventory is empty.")

    # Display all actions in the stack (inventory updates)
    def display_stack(self):
        self.order_stack.display()

# Example usage of Warehouse Inventory with Stack:
warehouse = WarehouseInventory(5)  # Maximum 5 products in the inventory

# Adding products
warehouse.add_product(1001, "Product A", 50, 2)
warehouse.add_product(1002, "Product B", 30, 1)
warehouse.add_product(1003, "Product C", 40, 3)

# Displaying current inventory
warehouse.display_inventory()

# Updating product quantities
warehouse.update_quantity(1001, 60)
warehouse.update_quantity(1002, 45)

# Removing a product from the inventory
warehouse.remove_product(1003)

# Displaying the updated inventory
warehouse.display_inventory()

# Displaying the action stack (order history of updates)
warehouse.display_stack()

# Undoing the last action (removing a product from the stack)
warehouse.order_stack.pop()  # Removes the last action
warehouse.display_stack()  # Shows the remaining actions in the stack
