import uuid

# Dictionary to store orders
orders = {}

def place_order(customer_name, items):
    """Places an order and generates a unique Order ID."""
    order_id = str(uuid.uuid4())  # Generate unique Order ID
    orders[order_id] = {"Customer": customer_name, "Items": items}
    print(f"\n✅ Order placed successfully! Your Order ID: {order_id}\n")

def view_orders():
    """Displays all orders."""
    if not orders:
        print("\n🚫 No orders placed yet.")
    else:
        print("\n📦 Order Summary:")
        for order_id, details in orders.items():
            print(f"🆔 Order ID: {order_id}\n👤 Customer: {details['Customer']}\n🛍 Items: {', '.join(details['Items'])}\n")

# Main Menu
while True:
    print("\n🛒 E-Commerce Order System")
    print("1️⃣ Place Order")
    print("2️⃣ View Orders")
    print("3️⃣ Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter your name: ")
        items = input("Enter items (comma-separated): ").split(",")
        place_order(name, [item.strip() for item in items])
    
    elif choice == "2":
        view_orders()
    
    elif choice == "3":
        print("\n🚪 Exiting the system. Thank you for shopping!")
        break
    
    else:
        print("\n⚠️ Invalid choice. Please enter 1, 2, or 3.")
