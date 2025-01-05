class WarehouseInventory:
    def __init__(self, capacity):
        self.capacity = capacity  # Maximum number of products the array can hold
        self.inventory = [None] * capacity  # Array to hold products, initialized to None
        self.size = 0  # Current number of products in the inventory

    # Add a new product to the inventory
    def add_product(self, product_id, name, quantity, priority):
        if self.size < self.capacity:
            self.inventory[self.size] = {
                "product_id": product_id,
                "name": name,
                "quantity": quantity,
                "priority": priority
            }
            self.size += 1
            print(f"Product {name} added successfully.")
        else:
            print("Inventory is full, cannot add more products.")

    # Update the stock quantity for a specific product by product_id
    def update_quantity(self, product_id, quantity):
        for i in range(self.size):
            if self.inventory[i]["product_id"] == product_id:
                self.inventory[i]["quantity"] = quantity
                print(f"Product ID {product_id} stock updated to {quantity}.")
                return
        print(f"Product ID {product_id} not found in the inventory.")

    # Search for a product by product_id
    def search_product(self, product_id):
        for i in range(self.size):
            if self.inventory[i]["product_id"] == product_id:
                return self.inventory[i]
        return None

    # Display the entire inventory
    def display_inventory(self):
        if self.size == 0:
            print("Inventory is empty.")
        else:
            print("Inventory List:")
            for product in self.inventory[:self.size]:
                print(f"ID: {product['product_id']}, Name: {product['name']}, "
                      f"Quantity: {product['quantity']}, Priority: {product['priority']}")

# Example usage:
warehouse = WarehouseInventory(5)  # Maximum of 5 products in the inventory

# Adding products to the inventory
warehouse.add_product(1001, "Product A", 50, 2)
warehouse.add_product(1002, "Product B", 20, 1)
warehouse.add_product(1003, "Product C", 30, 3)

# Display the inventory
warehouse.display_inventory()

# Update quantity for a product
warehouse.update_quantity(1001, 60)

# Search for a product by ID
product = warehouse.search_product(1002)
if product:
    print(f"Found: {product['name']}, Quantity: {product['quantity']}, Priority: {product['priority']}")
else:
    print("Product not found.")

# Display the updated inventory
warehouse.display_inventory()
