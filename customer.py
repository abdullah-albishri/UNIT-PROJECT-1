from datetime import datetime

def validate_plate_number(plate_num: str) -> bool:
    """
    Validate a car plate string.
    Format: 1–3 letters (A–Z) followed by 1–4 digits.
    """
    if not plate_num:
        return False

    plate_num = plate_num.strip().upper()

    letters = ""
    numbers = ""
    letters_part = True

    for char in plate_num:
        if char.isalpha() and letters_part:
            letters += char
        elif char.isdigit() and letters:
            numbers += char
            letters_part = False
        else:
            return False

    if not (1 <= len(letters) <= 3):
        return False
    if not (1 <= len(numbers) <= 4):
        return False

    return True


class Customer:
    def __init__(self, name: str, plate: str):
        name = (name or "").strip()
        plate = (plate or "").strip().upper()

        if not name:
            raise ValueError("Name cannot be empty")

        if not validate_plate_number(plate):
            raise ValueError("Plate must consist of 1–3 letters followed by 1–4 digits")

        self.name = name
        self.plate = plate
        self.last_visit = None
        self.orders = []
        self.visits = 0
        self.loyalty_point = 0

    def __repr__(self) -> str:
        return f"<Customer name={self.name!r} plate={self.plate!r} visits={self.visits}>"

    def add_visit(self):
        '''function to add visits'''
        self.last_visit = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.visits += 1
        self.loyalty_point += 10

    def add_order(self, orders: str):
        '''function to takes order'''
        if orders.strip():
            self.orders.append(orders)
        else:
            print('order cannot be empty')

    
    def show_loyalty_point(self):
        print(f"Loyalty points: {self.loyalty_point}")

    def to_dict(self):
        '''to save in Dictionary'''
        return {
            'name': self.name,
            'plate': self.plate,
            'last_visit': self.last_visit,
            'orders': self.orders,
            'visits': self.visits,
            'loyalty_point': self.loyalty_point
        }
