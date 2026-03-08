import json # library used to read and write json files 
import os # library used to check if files exist in the system
from customer import Customer
from datetime import datetime

#creat Restaurant class 
class Restaurant :

    def __init__(self , data_file='Customers.json'):
        '''constructor method that runs when we create an object'''
        self.data_file=data_file #File where customer data will be stored
        self.customers = {} #dictionary to customer 
        
        # menu coffee shop 
        self.menu ={
            1:{'name':'coffee day','price':10},
            2:{'name':'V60','price':20},
            3:{'name':'latte','price':15},
            4:{'name':'Mocha','price':25}
        }
        #load exist customer from file
        self.load_data()

    # load customer data from JSON file 
    def load_data(self):
        #check if json file already exists
        if not os.path.exists(self.data_file):
            self.customers = {}
            return
        try:
            #open the in read mode
            with open(self.data_file,'r')as file:
                data = json.load(file) #load JSON data into a pyhton dictionary
                for plate,i in data.items(): # loop to saved each customer 
                    customer = Customer (i['name'],plate) #creat a new customer 
                    customer.visits=i.get('visits',0) #add visit to customer 
                    customer.loyalty_point= (i.get('loyalty_point',0)) #add loyalty point to customer 
                    customer.orders=i.get('orders',[]) #add a new order to customer 
                    self.customers[plate]= customer #add the customer to dictionary
        except (json.JSONDecodeError,IOError): #if have something wrong , we start with empty data
            print('Error loading data file. string with empty data')
            self.customers= {} 

    def save_data(self):
        '''save customer data to JSON file '''
        try:
            #open JSON file in write mode 
            with open(self.data_file,'w')as file:
                #cuustomer dara in dictionary 
                json.dump(
                    {plate : customer.to_dict()
                     for plate, customer in self.customers.items()},
                     file,
                     indent=4,
                     ensure_ascii=False
                )
        except IOError: #if wrong save data 
            print('Error save data')

    def get_customer(self,name:str ,plate:str)->Customer:
        '''To get customer existing or a new customer '''
        plate = plate.upper() #plate lower letters to upper letters

        #if the customer existing ,we return 
        if plate in self.customers:
            customer = self.customers[plate]
            print(f'welcome back{customer.name}. we miss you :)')
        else :
            #if the customer new , we added 
            customer = Customer(name,plate )
            self.customers[plate]= customer 
            print('Done new customer added ')

        customer.add_visit() #added visit to customer 
        self.save_data() #save data 
        return customer 
    
    def show_menu(self):
        '''To show menu'''
        print('\n Coffee menu')
        for key,item in self.menu.items():
            print (f'{key} - {item['name']} ---> {item['price']} SAR')
    
    def order_from_menu(self,customer:Customer):
        '''function order from menu'''
        try:
            self.show_menu() #show menu to customer 
            choice = int(input('Choose item number : ')) # Enter drink number

            if choice not in self.menu: #if customer choice wrong number 
                print('Invalid choice ')
                return
            
            item = self.menu[choice] # return drink data 
            customer.add_order(item['name']) # add the order to customer 
            self.save_data() # save data 
            print(f'{item['name']} added to your order')

        except ValueError: # if enter invalid number  
            print('please enter a valid number')


    def show_oders(self , customer:Customer):
        '''function for show last order'''
        if not customer.orders:
            print('Not found your oders')
            return 
        
        print('\n previous oders : ')
        for i ,order in enumerate(customer.orders,start=1):
            print(f'{i}.{order}')

    
    def calculate_total(self, items): 
        '''function for colculate total price '''
        total = 0 
        for item in items:
            for menu_item in self.menu.values():
                if menu_item['name']==item:
                    total += menu_item['price']
        return total
    

    def apply_loyalty_discount(self, customer:Customer , total ):
        '''function for loyalty discount '''

        if customer.loyalty_point < 100:# if point less 100 , no discount
            print('You donot have much loyalty point ')
            return total
        
        print(f'\n you have {customer.loyalty_point} loyalty points')
        use_points = input('DO you want to use points for discount ? (y/n):')
        if use_points.lower()=='y':
            discount_units = customer.loyalty_point // 100
            discount = discount_units * 10 

            total -= discount
            customer.loyalty_point -= discount_units *100 # every 100 points = discount 10 SAR

            if total < 0:
                total = 0
            print(f'Discount applied : {discount} SAR')
        if use_points.lower() =='n':
            print(f'your have {customer.loyalty_point} point loyalty')
        return total
    
    def show_bill(self, customer):
        '''function fer show bill'''
        if not customer.orders:
            print('No order found')
            return
        print('\n --- Bill summary ---')
        for order in customer.orders:
            print(order)
        
        total = self.calculate_total(customer.orders)
        total = self.apply_loyalty_discount(customer, total)

        print(f'\nTotal price {total} SAR')
        self.save_data()


    def show_customer_summary(self , customer:Customer):
        '''function for show customer summary'''
        print('\n ===== Customer Summary ===== ')
        print(f'Name : {customer.name}')
        print(f'Plate : {customer.plate}')
        print(f'Last_visit : {customer.last_visit}')
        print(f'visits : {customer.visits}')
        print (f'Loyalty point : {customer.loyalty_point}')




