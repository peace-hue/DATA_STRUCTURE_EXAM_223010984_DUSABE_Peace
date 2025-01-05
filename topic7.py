class Product:
    def __init__(self, product_id, product_name, quantity, priority):
        self.product_id = product_id
        self.product_name = product_name
        self.quantity = quantity
        self.priority = priority  # Priority level: lower number means higher priority
    
    def __repr__(self):
        return f"ID: {self.product_id}, Name: {self.product_name}, Quantity: {self.quantity}, Priority: {self.priority}"

class WarehouseInventory:
    def __init__(self):
        self.products = []  # List to store products

    # Add a new product to the inventory
    def add_product(self, product_id, product_name, quantity, priority):
        product = Product(product_id, product_name, quantity, priority)
        self.products.append(product)

    # Selection Sort to sort products based on priority (ascending order: lower priority is better)
    def selection_sort(self):
        n = len(self.products)
        for i in range(n):
            # Find the index of the product with the lowest priority
            min_idx = i
            for j in range(i + 1, n):
                if self.products[j].priority < self.products[min_idx].priority:
                    min_idx = j
            # Swap the found product with the first product of the unsorted part
            self.products[i], self.products[min_idx] = self.products[min_idx], self.products[i]

    # Display all products in the inventory
    def display_inventory(self):
        if self.products:
            print("Warehouse Inventory (sorted by priority):")
            for product in self.products:
                print(product)
        else:
            print("Inventory is empty.")

# Example usage:
warehouse = WarehouseInventory()

# Add products to the warehouse inventory
warehouse.add_product(1001, "Product A", 50, 2)
warehouse.add_product(1002, "Product B", 30, 1)
warehouse.add_product(1003, "Product C", 40, 3)
warehouse.add_product(1004, "Product D", 20, 1)

# Display unsorted inventory
print("Unsorted Inventory:")
warehouse.display_inventory()

# Sort the inventory based on priority using Selection Sort
warehouse.selection_sort()

# Display sorted inventory
print("\nSorted Inventory (based on priority):")
warehouse.display_inventory()
