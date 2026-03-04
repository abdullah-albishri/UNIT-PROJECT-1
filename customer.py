

class Customer:
    def __init__(self, name:str ,plate:str , ):
        try:
            if not plate.strip():
                raise ('the plate must be letters and numbers')
            if not name.strip():
                return('the name cannot be empty')
            self.name=name
            self.plate = plate
            self.visits = 0 
            self.loyalty_point = 0 
            self.order = []
        except ValueError as e:
            print(f'input erorr : {e}') 
            raise


    def add_visit(self):
        self.visits +=1
        self.loyalty_point +=10

    def add_order(self , orders:str):
        if orders.strip():
            self.orders.append(orders)
        else:
            print('order cannot be empty')

    def to_dict(self):
        return{
            'name':self.name,
            'plate':self.plate,
            'visits':self.visits,
            'loyalty_point':self.loyalty_point,
            self.orders
        }

        

        

