from  datetime import datetime

#plate number validtion function 
#--------------------------------------
def validate_plate_number(plate_num: str) -> bool:
    """
    Valid plate format:
    - Starts with 1 to 3 letters
    - Followed by 1 to 4 numbers
    - No spaces or special characters
    """
    # for user if dont't enter any value 
    if not plate_num: 
        return False 
        
    letters = ''   
    numbers= ''   
    letters_part = True   # to help us found : Are we currently in the letters section or have we moved on to the numbers section?

    for char in plate_num:   #each letters and numbers in loops 
        if char.isalpha() and letters_part :
            letters+= char  #if char in plate letter we will to added letters 
        elif char.isdigit() and letters:
            numbers += char  #if char in plate is number and check we have letter befor number then we will added to numbers 
            letters_part = False  #We change letter part to False to prevent letters from following numbers.
        else:
            return False 
    # we check that the letters and numbers of char is : At least 1 and At most 3 .        
    if not (1<= len(letters)<=3):  
            return False 
    if not (1<= len(numbers)<=4):
        return False
    return True


#creat class Customer
class Customer:
    def __init__(self, name:str ,plate:str , ):
        try:
            if not validate_plate_number(plate): # we check the plate contains numbers and letters
                raise ('the plate must be letters At least 1 to 3 and numbers At least 1 to 4')
            if not name.strip(): # نتاكد ان الاسم صحيح وبدون مسافة
                return('the name cannot be empty')
            self.name=name
            self.plate = plate.upper() #confirm the letters is capital 
            self.last_visit = None 
            self.orders = []
            self.visits = 0
            self.loyalty_point = 0 
            
        except ValueError as e:
            print(f'input erorr : {e}') 
            raise # نمنع ادخال اي بيانات خاطئة 


    def add_visit(self): 
        ''' function to add visits'''
        self.last_visit = datetime.now().strftime("%Y-%m-%d %H:%M:%S")# to regester last visit with library datetime
        self.visits +=1 # every visit we add one to visit 
        self.loyalty_point +=10 #every visit we add 10-point to loyalty 
         


    def add_order(self , orders:str): 
        '''  function to takes order'''
        if orders.strip():
            self.orders.append(orders)
        else:
            print('order cannot be empty')

    def to_dict(self):
        ''' to save in Dictionary'''
        # to Show it in Dictionary
        return{
            'name':self.name,
            'plate':self.plate,
            'last_visit':self.last_visit,
            'orders':self.orders,
            'visits':self.visits,
            'loyalty_point':self.loyalty_point    
        }

#maybe update remmber

        

        

