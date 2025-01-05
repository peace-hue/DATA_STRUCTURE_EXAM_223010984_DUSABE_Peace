class OrderNode:
    def __init__(self, order_id, product_name, quantity, priority):
        self.order_id = order_id
        self.product_name = product_name
        self.quantity = quantity
        self.priority = priority
        self.next = None  # Points to the next node in the list

class SinglyLinkedList:
    def __init__(self, capacity):
        self.capacity = capacity  # Maximum number of orders allowed in the list
        self.head = None  # Head of the linked list
        self.size = 0  # Number of orders currently in the list

    # Add a new order to the linked list
    def add_order(self, order_id, product_name, quantity, priority):
        if self.size >= self.capacity:
            print("Order limit reached. Cannot add more orders.")
            return

        new_order = OrderNode(order_id, product_name, quantity, priority)
        
        # If the list is empty, new order will be the first node (head)
        if self.head is None:
            self.head = new_order
        else:
            # Add the new order at the end of the list
            current = self.head
            while current.next:
                current = current.next
            current.next = new_order
        
        self.size += 1
        print(f"Order {order_id} added successfully.")

    # Update the order quantity and/or priority by order_id
    def update_order(self, order_id, quantity=None, priority=None):
        current = self.head
        while current:
            if current.order_id == order_id:
                if quantity is not None:
                    current.quantity = quantity
                if priority is not None:
                    current.priority = priority
                print(f"Order {order_id} updated.")
                return
            current = current.next
        print(f"Order {order_id} not found.")

    # Search for an order by order_id
    def search_order(self, order_id):
        current = self.head
        while current:
            if current.order_id == order_id:
                return current
            current = current.next
        return None

    # Display all orders in the linked list
    def display_orders(self):
        if self.size == 0:
            print("No orders in the system.")
        else:
            print("Orders List:")
            current = self.head
            while current:
                print(f"Order ID: {current.order_id}, Product: {current.product_name}, "
                      f"Quantity: {current.quantity}, Priority: {current.priority}")
                current = current.next

# Example usage:
warehouse_orders = SinglyLinkedList(5)  # Maximum of 5 orders

# Add orders to the warehouse
warehouse_orders.add_order(1001, "Product A", 50, 2)
warehouse_orders.add_order(1002, "Product B", 30, 1)
warehouse_orders.add_order(1003, "Product C", 20, 3)

# Display all orders
warehouse_orders.display_orders()

# Update an order
warehouse_orders.update_order(1002, quantity=40, priority=2)

# Search for an order
order = warehouse_orders.search_order(1003)
if order:
    print(f"Found: Order ID {order.order_id}, Product: {order.product_name}, "
          f"Quantity: {order.quantity}, Priority: {order.priority}")
else:
    print("Order not found.")

# Display the updated orders list
warehouse_orders.display_orders()
