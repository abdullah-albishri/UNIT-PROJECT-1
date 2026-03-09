from restaurant import Restaurant
from customer import validate_plate_number
from utils import info, success, warning, error, colored

def main():
    '''This function is the starting point of the program.'''
    my_restaurant = Restaurant()  # create restaurant object (stores customers, menu, orders, etc.)

    while True:
        print(colored("\n--- DriveGo ---", "\033[96m"))  # cyan header
        print("1. New Customer")
        print("2. Make Order")
        print("3. Show Customer Summary")
        print("4. List All Customers")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter customer name: ").strip()
            while True:
                plate = input("Enter plate number: ").strip().upper()
                if validate_plate_number(plate):
                    break
                print(error("Invalid plate format. Use 1–3 letters followed by 1–4 digits."))

            try:
                my_restaurant.get_customer(name, plate)
            except Exception as e:
                print(error(str(e)))

        elif choice == "2":
            plate = input("Enter plate number: ").strip().upper()

            if plate in my_restaurant.customers:
                customer = my_restaurant.customers[plate]
                print(success(f"\nWelcome {customer.name}!"))

                current_order = []
                skip_menu = False  # flag: whether to skip the menu and go directly to the bill

                if customer.orders:
                    # last_order contains all items from the last order session
                    last_order = customer.orders[-1]
                    last_time = customer.last_visit
                    print(f"Your last visit was: {''.join(last_time)}")
                    print(f"Your last order was: {', '.join(last_order)}")

                    repeat = input("Do you want the same order? (y/n): ")

                    if repeat.lower() == "y":
                        # add all items from the previous order
                        current_order.extend(last_order)

                        # ask if the customer wants to add more items
                        add_more = input("Do you want to add more items to your order? (y/n): ")
                        if add_more.lower() != "y":
                            skip_menu = True  

                # show the menu only if skip_menu = False
                if not skip_menu:
                    while True:
                        my_restaurant.show_menu()

                        try:
                            item_choice = int(input("Choose item number: "))

                            # cancel option
                            if item_choice == 0:
                                if current_order:
                                    print(info("No items added. Keeping your previous order."))
                                else:
                                    print(warning("Order cancelled."))
                                break

                            if item_choice in my_restaurant.menu:
                                item = my_restaurant.menu[item_choice]["name"]
                                current_order.append(item)
                                print(f"{item} added to your order")
                            else:
                                print("Invalid choice")

                        except ValueError:
                            print("Please enter a valid number")
                            continue

                        more = input("Do you want to add another item? (y/n): ")

                        if more.lower() == "n":
                            break

                if current_order:
                    customer.orders.append(current_order)

                    customer.add_visit()

                    total = my_restaurant.calculate_total(current_order)
                    total = my_restaurant.apply_loyalty_discount(customer, total)

                    print("\n--- Current Bill ---")
                    for item in current_order:
                        print(item)

                    print(f"\nTotal price: {total} SAR")

                    my_restaurant.save_data()
                    my_restaurant.show_customer_summary(customer)

                else:
                    print("No order made")

            else:
                print("Customer not found! Please register first.")

        elif choice == "3":
            plate = input("Enter plate number: ").strip().upper()
            if plate in my_restaurant.customers:
                my_restaurant.show_customer_summary(my_restaurant.customers[plate])
            else:
                print(warning("Customer not found."))

        elif choice == "4":
            my_restaurant.list_customers()

        elif choice == "5":
            print(success("Thank you for using DriveGo"))
            break

        else:
            print(warning("Invalid choice. Try again."))


if __name__ == "__main__":
    main()