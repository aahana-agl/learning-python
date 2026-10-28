print("=== Grocery Billing Queue ===\n")

low_price_items = 0
medium_price_items = 0
high_price_items = 0
customers_served = 0
total_sales = 0
billing = True

while billing:
    name = input()
    item_count = int(input())

    if item_count <= 0:
        print("Message")
        continue

    customer_total = 0
    item_number = 1

    while item_number <= item_count:
        item_name = input()
        price = int(input())
        quantity = int(input())

        if price <= 0 or quantity <= 0:
            print("Message")
            continue

        item_total = price * quantity
        print(f"{item_name}: {quantity} x {price} = {item_total}")
        customer_total += item_total

        if price < 50:
            low_price_items += quantity
        elif 50 <= price <= 100:
            medium_price_items += quantity
        else:
            high_price_items += quantity

        item_number += 1

    customers_served += 1
    total_sales += customer_total
    print(customer_total)

    answer = input()
    if answer != "yes":
        billing = False

for band_name, band_count in [("low", low_price_items), ("medium", medium_price_items), ("high", high_price_items)]:
    for _ in range(band_count):
        print("*", end="")
    print()

print(customers_served)
print(total_sales)
