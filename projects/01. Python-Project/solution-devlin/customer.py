############################# CUSTOMER CLASS #############################################
class Customer(dict):

    def __init__(self, acct_id, first_name= False, last_name=False, password="", checking=False, savings=False, active=True, overdraft_count=0):
        self.id = acct_id
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.checking = checking
        self.savings = savings
        self.active = active
        self.overdraft_count = overdraft_count
    
    def __str__(self):
        return f" Account info: {self.id} {self.first_name} {self.last_name} {self.password} {self.checking} {self.savings} {self.active} {self.overdraft_count}"

    # UPDATE NAME, PASSWORD, ETC.
    def update_customer_info(self, field, value):
        print("updating customer info", field, value)