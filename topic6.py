class TreeNode:
    def __init__(self, category_name, product_info=None):
        self.category_name = category_name  # Name of the category or subcategory
        self.product_info = product_info  # Info about products (could be a list of products)
        self.children = []  # List of child nodes (subcategories)

class WarehouseTree:
    def __init__(self):
        self.root = None  # The root of the tree

    # Add a new category or subcategory under a parent node
    def add_category(self, parent_category_name, category_name, product_info=None):
        if self.root is None:
            self.root = TreeNode(category_name, product_info)  # Set root if the tree is empty
            print(f"Root Category '{category_name}' added.")
        else:
            parent_node = self.search_category(self.root, parent_category_name)
            if parent_node:
                new_node = TreeNode(category_name, product_info)
                parent_node.children.append(new_node)
                print(f"Category '{category_name}' added under '{parent_category_name}'.")
            else:
                print(f"Parent category '{parent_category_name}' not found.")

    # Search for a category in the tree (DFS approach)
    def search_category(self, node, category_name):
        if node is None:
            return None
        if node.category_name == category_name:
            return node
        
        # Search in children
        for child in node.children:
            result = self.search_category(child, category_name)
            if result:
                return result
        return None

    # Display the entire inventory tree (recursive)
    def display_inventory(self, node=None, level=0):
        if node is None:
            node = self.root
        if node is not None:
            print("  " * level + f"Category: {node.category_name}")
            if node.product_info:
                print("  " * (level + 1) + f"Products: {node.product_info}")
            # Display all subcategories (children)
            for child in node.children:
                self.display_inventory(child, level + 1)

# Example usage:

# Initialize the warehouse tree
warehouse_inventory = WarehouseTree()

# Add root category (e.g., Electronics)
warehouse_inventory.add_category(None, "Electronics", product_info=None)

# Add subcategories under Electronics
warehouse_inventory.add_category("Electronics", "Smartphones", product_info=["iPhone", "Samsung Galaxy", "OnePlus"])
warehouse_inventory.add_category("Electronics", "Laptops", product_info=["MacBook", "Dell XPS", "HP Pavilion"])

# Add another top-level category (e.g., Furniture)
warehouse_inventory.add_category(None, "Furniture", product_info=None)

# Add subcategories under Furniture
warehouse_inventory.add_category("Furniture", "Chairs", product_info=["Office Chair", "Gaming Chair", "Rocking Chair"])
warehouse_inventory.add_category("Furniture", "Tables", product_info=["Dining Table", "Coffee Table", "Study Table"])

# Display the inventory tree
warehouse_inventory.display_inventory()

# Search for a category
category = warehouse_inventory.search_category(warehouse_inventory.root, "Laptops")
if category:
    print(f"\nCategory '{category.category_name}' found!")
else:
    print("\nCategory not found.")
