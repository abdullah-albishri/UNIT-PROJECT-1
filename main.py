from restaurant import Restaurant

def main():

    my_restaurant = Restaurant()

    while True:

        print("\n--- DriveGo ---")
        print("1. New/Check-in Customer")
        print("2. Make Order")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":

            name = input("Enter customer name: ")
            plate = input("Enter plate number: ")

            my_restaurant.get_customer(name, plate)


        elif choice == "2":
            plate = input("Enter plate number: ").upper()
            if plate in my_restaurant.customers:
                customer = my_restaurant.customers[plate]

                print(f"\nWelcome back {customer.name}!")

                current_order = []

                if customer.orders:

                    last_order = customer.orders[-1]
                    print(f"Your last order was: {last_order}")

                    repeat = input("Do you want the same order? (y/n): ")

                    if repeat.lower() == "y":
                        current_order.append(last_order)

                while True:

                    my_restaurant.show_menu()

                    try:
                        item_choice = int(input("Choose item number: "))

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

                    customer.orders.append(current_order[-1])
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

            print("Thank you for using Smart Drive Thru!")
            break

        else:

            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()