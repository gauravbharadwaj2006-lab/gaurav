orders = []
n = int(input("Enter number of customers/orders: "))
for i in range(n):
    print(f"\nOrder {i+1}")
    customer_name = input("Enter customer name: ")
    
    m = int(input("Enter number of items ordered: "))
    items = []
    order_total = 0
    for j in range(m):
        print(f"  Item {j+1}")
        item_name = input("  Enter item name: ")
        price = float(input("  Enter item price: "))
        quantity = int(input("  Enter quantity: "))
        cost = price * quantity
        order_total += cost
        items.append({
            "name": item_name,
            "price": price,
            "quantity": quantity,
            "cost": cost
        })
    orders.append({
        "customer": customer_name,
        "items": items,
        "total": order_total
    })
total_revenue = 0
print("\n----- ORDER SUMMARY -----")
for order in orders:
    print(f"\nCustomer: {order['customer']}")
    for item in order["items"]:
        print(f"  {item['name']} - {item['quantity']} x {item['price']} = {item['cost']}")
    print(f"  Order Total: {order['total']}")
    total_revenue += order["total"]
print("\n--------------------------")
print(f"Total Revenue for the Day: {total_revenue}")
