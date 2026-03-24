items = []
n = int(input("Enter number of items: "))
for i in range(n):
    print(f"\nItem {i+1}")
    name = input("Enter item name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    items.append({
        "name": name,
        "price": price,
        "quantity": quantity
    })
total_bill = 0
most_expensive = items[0]
for item in items:
    item_total = item["price"] * item["quantity"]
    total_bill += item_total
    if item["price"] > most_expensive["price"]:
        most_expensive = item
discount = 0
if total_bill > 2000:
    discount = total_bill * 0.10   
    total_bill -= discount
print("\n----- BILL SUMMARY -----")
for item in items:
    print(f"{item['name']} - {item['quantity']} x {item['price']} = {item['quantity'] * item['price']}")

print("\nMost expensive item:", most_expensive["name"], "Price:", most_expensive["price"])

print(f"\nDiscount applied: {discount}")
print(f"Final Total Bill: {total_bill}")
