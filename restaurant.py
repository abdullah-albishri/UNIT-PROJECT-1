import json
import os
from datetime import datetime

from customer import Customer, validate_plate_number
from utils import Fore, info, success, warning, error, colored

class Restaurant:

    def __init__(self, data_file='Customers.json'):
        self.data_file = data_file
        self.customers = {}

        self.menu = {
            1: {'name': 'coffee day', 'price': 10},
            2: {'name': 'V60', 'price': 20},
            3: {'name': 'latte', 'price': 15},
            4: {'name': 'Mocha', 'price': 25}
        }
        self.load_data()

    def load_data(self):
        if not os.path.exists(self.data_file):
            self.customers = {}
            return
        try:
            with open(self.data_file, 'r') as file:
                data = json.load(file)
                for plate, i in data.items():
                    plate_key = plate.upper()
                    try:
                        customer = Customer(i['name'], plate_key)
                    except ValueError:
                        continue
                    customer.visits = i.get('visits', 0)
                    customer.loyalty_point = i.get('loyalty_point', 0)
                    customer.last_visit = i.get('last_visit', None)
                    raw_orders = i.get('orders', [])
                    if raw_orders and isinstance(raw_orders[0], str):
                        customer.orders = [raw_orders]
                    else:
                        customer.orders = raw_orders
                    self.customers[plate_key] = customer
        except (json.JSONDecodeError, IOError):
            print(error('Error loading data file; starting with empty data'))
            self.customers = {}

    def save_data(self):
        try:
            with open(self.data_file, 'w') as file:
                json.dump(
                    {plate: customer.to_dict()
                     for plate, customer in self.customers.items()},
                    file,
                    indent=4,
                    ensure_ascii=False
                )
        except IOError:
            print(error('Error saving data'))

    def get_customer(self, name: str, plate: str) -> Customer:
        name = (name or "").strip()
        plate = (plate or "").strip().upper()

        if not validate_plate_number(plate):
            raise ValueError('Invalid plate format')
        if not name:
            raise ValueError('Name cannot be empty')

        if plate in self.customers:
            customer = self.customers[plate]
            print(success(f"Welcome back {customer.name}!"))
        else:
            customer = Customer(name, plate)
            self.customers[plate] = customer
            print(success('Done, new customer added'))
        self.save_data()
        return customer

    def show_menu(self):
        print(colored('\n Coffee menu', Fore.MAGENTA))
        for key, item in self.menu.items():
            print(f"{key} - {item['name']} ---> {item['price']} SAR")
        print("0 - Cancel")

    def order_from_menu(self, customer: Customer):
        try:
            self.show_menu()
            choice = int(input('Choose item number: '))

            if choice not in self.menu:
                print(warning('Invalid choice'))
                return

            item = self.menu[choice]
            customer.add_order(item['name'])
            self.save_data()
            print(success(f"{item['name']} added to your order"))

        except ValueError:
            print(error('Please enter a valid number'))

    def show_orders(self, customer: Customer):
        if not customer.orders:
            print(info('No previous orders found'))
            return
        print(colored('\nPrevious orders:', Fore.BLUE))
        for i, order in enumerate(customer.orders, start=1):
            print(f'{i}. {order}')

    def calculate_total(self, items):
        total = 0
        for item in items:
            for menu_item in self.menu.values():
                if menu_item['name'] == item:
                    total += menu_item['price']
        return total

    def apply_loyalty_discount(self, customer: Customer, total):
        if customer.loyalty_point < 100:
            print(info('You do not have enough loyalty points'))
            return total

        print(success(f"\nYou have {customer.loyalty_point} loyalty points"))
        use_points = input('Do you want to use points for discount? (y/n): ')
        if use_points.lower() == 'y':
            discount_units = customer.loyalty_point // 100
            discount = discount_units * 10

            total -= discount
            customer.loyalty_point -= discount_units * 100
            if total < 0:
                total = 0
            print(success(f'Discount applied: {discount} SAR'))
        elif use_points.lower() == 'n':
            print(info(f'You have {customer.loyalty_point} loyalty points'))
        return total

    def show_bill(self, customer):
        if not customer.orders:
            print('No order found')
            return
        print('\n --- Bill summary ---')
        all_items = [item for session in customer.orders for item in session]
        for order in all_items:
            print(order)
        total = self.calculate_total(all_items)
        total = self.apply_loyalty_discount(customer, total)
        print(f'\nTotal price {total} SAR')
        self.save_data()

    def list_customers(self):
        if not self.customers:
            print(info('No customers registered yet'))
            return
        print(colored('\nRegistered customers:', Fore.BLUE))
        for plate, cust in self.customers.items():
            print(f"{plate} - {cust.name} ({cust.visits} visits)")

    def show_customer_summary(self, customer: Customer):
        print(colored('\n===== Customer Summary =====', Fore.CYAN))
        print(f'Name         : {customer.name}')
        print(f'Plate        : {customer.plate}')
        print(f'Last visit   : {customer.last_visit}')
        print(f'Visits       : {customer.visits}')
        print(f'Loyalty pts  : {customer.loyalty_point}')
