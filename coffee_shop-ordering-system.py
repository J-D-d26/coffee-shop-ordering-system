class Coffee:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Order:
    def __init__(self):
        self.items = {}

    # add item with quantity
    def add_item(self, coffee, quantity):
        if coffee.name in self.items:
            self.items[coffee.name]["qty"] += quantity
        else:
            self.items[coffee.name] = {
                "price": coffee.price,
                "qty": quantity
            }

        print(f"{quantity} {coffee.name}(s) added to your order.")

    # remove item
    def remove_item(self, coffee_name):
        if coffee_name in self.items:
            del self.items[coffee_name]
            print(f"{coffee_name} removed from order.")
        else:
            print("Item not found in order.")

    # calculate total
    def total(self):
        return sum(v["price"] * v["qty"] for v in self.items.values())

    # show order
    def show_order(self):
        if not self.items:
            print("No items in order.")
            return

        print("\n----- Your Order -----")
        for i, (name, details) in enumerate(self.items.items(), 1):
            price = details["price"]
            qty = details["qty"]
            print(f"{i}. {name} x{qty} - ${price*qty}")

        print("----------------------")
        print(f"Total: ${self.total()}\n")

    # checkout
    def checkout(self):
        if not self.items:
            print("Your cart is empty.")
            return

        self.show_order()
        confirm = input("Proceed to checkout? (yes/no): ").lower()

        if confirm == "yes":
            print("\n🧾 Receipt")
            self.show_order()
            print("Thank you for your order ☕")
            self.items.clear()
        else:
            print("Checkout cancelled.")


def main():
    menu = [
        Coffee("Espresso", 2.5),
        Coffee("Latte", 3.5),
        Coffee("Cappuccino", 3.0),
        Coffee("Americano", 2.0)
    ]

    order = Order()

    while True:
        print("\n===== Coffee Menu =====")

        for i, coffee in enumerate(menu, 1):
            print(f"{i}. {coffee.name} - ${coffee.price}")

        print("5. View Order")
        print("6. Remove Item")
        print("7. Checkout")
        print("8. Exit")

        choice = input("Choose option: ")

        if choice in ["1", "2", "3", "4"]:
            qty = int(input("Enter quantity: "))
            order.add_item(menu[int(choice) - 1], qty)

        elif choice == "5":
            order.show_order()

        elif choice == "6":
            name = input("Enter coffee name to remove: ")
            order.remove_item(name)

        elif choice == "7":
            order.checkout()

        elif choice == "8":
            print("Thanks for visiting ☕")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()


