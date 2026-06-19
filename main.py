import csv

products = {}

while True:
    print("\n=== Inventory & Sales Management System ===")
    print("1 - Add Product")
    print("2 - Show Products")
    print("3 - Sell Product")
    print("4 - Revenue Report")
    print("5 - Save to CSV")
    print("6 - Exit")

    choice = input("Select: ")

    if choice == "1":
        name = input("Product Name: ")
        price = float(input("Price: "))
        stock = int(input("Stock: "))

        products[name] = {
            "price": price,
            "stock": stock,
            "sold": 0
        }

        print("Product Added!")

    elif choice == "2":
        print("\n=== Products ===")

        for name, info in products.items():
            print(
                f"{name} | Price: {info['price']} | Stock: {info['stock']}"
            )

    elif choice == "3":
        name = input("Product Name: ")

        if name in products:

            qty = int(input("Quantity: "))

            if qty <= products[name]["stock"]:

                products[name]["stock"] -= qty
                products[name]["sold"] += qty

                print("Sale Completed!")

            else:
                print("Not enough stock!")

        else:
            print("Product not found!")

    elif choice == "4":

        total_revenue = 0

        for name, info in products.items():

            revenue = info["sold"] * info["price"]

            total_revenue += revenue

            print(
                f"{name} Revenue: {revenue}"
            )

        print(
            f"\nTotal Revenue: {total_revenue}"
        )

    elif choice == "5":

        with open(
            "products.csv",
            "w",
            newline=""
        ) as file:

            writer = csv.writer(file)

            writer.writerow([
                "Product",
                "Price",
                "Stock",
                "Sold"
            ])

            for name, info in products.items():

                writer.writerow([
                    name,
                    info["price"],
                    info["stock"],
                    info["sold"]
                ])

        print("Saved to CSV!")

    elif choice == "6":
        print("Program Closed")
        break

    else:
        print("Invalid Selection")