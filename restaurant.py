import json
import os
from customer import Customer

class Restaurant :
    def __init__(self , data_file='Customer.json'):
        self.data_file=data_file
        self.customer = {}

        self.menu ={
            1:{'name':'coffee day','price':10},
            2:{'name':'V60','price':20},
            3:{'name':'latte','price':15},
            4:{'name':'Mocha','price':25}
        }
        self.load.data()

    
    def load_data(self):
        if not os.path.exists(self.data_file):
            self.customer = {}
            return
        try:
            with open(self.data_file,'r')as file:
                data = json.load(file)
                for plate,i in data.items():
                    customer = Customer (i['name'],plate)
                    customer.visits=i.get('visits',0)
                    customer.loyalty_point= (i.get('loyalty_point',0))
                    customer.orders=i.get('orders',[])
                    self.customer[plate]= customer


