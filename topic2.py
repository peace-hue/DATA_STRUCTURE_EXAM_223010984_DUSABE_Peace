class BSTNode:
    def __init__(self, product_id, name, quantity, priority):
        self.product_id = product_id
        self.name = name
        self.quantity = quantity
        self.priority = priority
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    # Insert a new product into the BST
    def insert(self, product_id, name, quantity, priority):
        self.root = self._insert_recursive(self.root, product_id, name, quantity, priority)
    
    def _insert_recursive(self, node, product_id, name, quantity, priority):
        if node is None:
            return BSTNode(product_id, name, quantity, priority)
        
        if product_id < node.product_id:
            node.left = self._insert_recursive(node.left, product_id, name, quantity, priority)
        else:
            node.right = self._insert_recursive(node.right, product_id, name, quantity, priority)
        
        return node
    
    # Search for a product by product_id
    def search(self, product_id):
        return self._search_recursive(self.root, product_id)
    
    def _search_recursive(self, node, product_id):
        if node is None or node.product_id == product_id:
            return node
        
        if product_id < node.product_id:
            return self._search_recursive(node.left, product_id)
        
        return self._search_recursive(node.right, product_id)
    
    # In-order traversal of the BST to display products
    def inorder_traversal(self):
        products = []
        self._inorder_recursive(self.root, products)
        return products
    
    def _inorder_recursive(self, node, products):
        if node:
            self._inorder_recursive(node.left, products)
            products.append((node.product_id, node.name, node.quantity, node.priority))
            self._inorder_recursive(node.right, products)

# Example usage:
bst = BST()
bst.insert(1001, "Product A", 50, 2)
bst.insert(1002, "Product B", 20, 3)
bst.insert(1000, "Product C", 10, 1)

# Search for a product
product = bst.search(1002)
if product:
    print(f"Found: {product.name}, Quantity: {product.quantity}, Priority: {product.priority}")
else:
    print("Product not found.")

# Display all products
products = bst.inorder_traversal()
for p in products:
    print(f"ID: {p[0]}, Name: {p[1]}, Quantity: {p[2]}, Priority: {p[3]}")
