import csv
from transaction import Transactions
from customer    import Customer
from history     import History

############################# HELPER FUNCTION #############################################
def show_dict_items(dictionary):
    return "\n".join([ f"{key}: {val}" for key, val in dictionary.items()])+":: User Choice => "

def invalid(item):
    options = { "number": "\nPlease choose a valid amount.", "choice": "\nPlease choose a valid option." }
    return options[item]

############################# BANK CLASS #####################################################
class Bank():
    acct_id = 0
    customers = []
    user = None
    user_session = None
    fieldnames = ['id', "first_name", 'last_name', "password", "checking", "savings", "active", "overdraft_count"]
    filename = "./bank.csv"

    def __init__(self):
        pass

    @classmethod
    def find_acct(cls, acct_id):
        for acct in cls.customers:
            if acct.id == acct_id:
                return acct
        return False



    # @classmethod
    # def deposit_transfer_amt_into_external_acct(cls, acct_id, acct_type, amount):
    #     for acct in cls.customers:
    #         if acct.id == acct_id


    @classmethod
    def load_accounts(cls):
        try: 
            with open(Bank.filename, "r") as file:
                contents = csv.DictReader(file)
                for row in contents:
                    customer = Customer(row)
                    Bank.customers.append(customer)
                    if customer.id >= Bank.acct_id:
                        Bank.acct_id = customer.id
        except csv.Error as e:
            print(e)
    
    @classmethod
    def update_data(self):
        with open(Bank.filename, 'w', newline='') as csvfile:
            try:
                writer = csv.DictWriter(csvfile, fieldnames=Bank.fieldnames)
                writer.writeheader()
                for row in Bank.customers:
                    writer.writerow(row.__dict__)
            except csv.Error as e:
                print(e)

    @classmethod
    def login(self):
        validated = False
        user_id   = None
        user_pass = None

        while not validated and (user_id != "Q" or user_pass != "Q"):
            # GET USER INFO: ID and PASSWORD
            user_id = input("\nPlease provide your account id or 'Q' to quit.\n:: Account ID => ")
            if user_id == "Q":
                Bank.user_session = "Q"
                return
            user_pass = input("\nPlease provide your account password or 'Q' to quit.\n:: Account Password => ")
            if user_pass == "Q":
                Bank.user_session = "Q"
                return
            
            # VALIDATE
            for acct in Bank.customers:
                if str(acct.id) == user_id and user_pass == acct.password:
                    validated = True
                    print(f"\nWelcome back, {acct.first_name} {acct.last_name}.")
                    Bank.user = acct
                    History.add_transaction_entry(2, acct)
            
            # ACCT NOT FOUND / INCORRECT INFO
            if not validated:
                print("\nPlease enter the correct credentials to login or 'Q' to quit.")

        return

    @classmethod
    def signup(self):
        new_user = Customer.get_new_user()

        # GET/SET USER INFO
        print("\nWe're delighted you would like to join us. Please provide the following information to start an account:")
        new_user["first_name"] = input("\nPlease provide your legal first name:\n:: User First Name => ")
        new_user["last_name"]  = input("\nPlease provide your legal last name:\n:: User Last Name => ")
        new_user["password"]   = input("\nPlease provide a password with at least 5 characters:\n:: User Password => ")
        
        # GET ACCT CHOICE
        acct_options_dict = {"1": "checking", "2": "savings", "Q": "Exit"}
        acct_choice = None
        while acct_choice not in acct_options_dict.keys():
            acct_choice = input(f"\nPlease choose an account to open:\n{show_dict_items(acct_options_dict)}")
            if acct_choice == "Q":
                Bank.user_session = "Q"
                return
            if acct_choice not in acct_options_dict.keys():
                print(invalid("choice"))

        # CREATE SUCCESSFUL => SET ACCT TO 0, SET ID, UPDATE BANK DATA
        Bank.acct_id += 1
        new_user["id"] = Bank.acct_id
        new_user[acct_options_dict[acct_choice]] = 0
        user_obj = Customer(new_user)
        Bank.customers.append(user_obj)
        Bank.user = user_obj
        Bank.update_data()
        print(f"Thank you, {user_obj.first_name} {user_obj.last_name}, for joining Gotham Bank!! Welcome!")
        return
        
    @classmethod
    def access_existing_account(self, acct_type):
        Transactions.user = Bank.user
        Transactions.user_session = Bank.user_session
        Transactions.update_accounts = Bank.update_data
        Transactions.find_acct = Bank.find_acct
        account_actions_dict = { "1": "Deposit", "2": "Withdraw", "3": "Transfer", "4": "Check Balance", "5": "Transactions History", "Q": "Exit\n" }
        acct_type = acct_type.lower()
        action = None
        input_msg = f"\nWhat would you like to do in your {acct_type}?"

        while action not in account_actions_dict.keys() and action != "Q" or action == "Y":
            action = input(f"{input_msg}\n{show_dict_items(account_actions_dict)}")
            if action == "1":
                Transactions.deposit(acct_type)
            if action == "2":
                Transactions.withdraw(acct_type)
            if action == "3":
                Transactions.transfer(acct_type)
            if action == "4":
                Transactions.get_balance(acct_type)
            if action == "5":
                History.get_user_history(Bank.user)
            if action == "Q":
                Bank.user_session = "Q"
                return
            action = Bank.ask_another_transaction()
            if action not in account_actions_dict.keys() and action != "Y":
                print(invalid("choice"))

    @classmethod
    def ask_another_transaction(self):
        options = { "Y": "Yes", "Q": "Exit\n" }
        msg = "Would you like another transaction?"
        action = None
        while action not in options.keys():
            action = input(f"\n{msg}\n{show_dict_items(options)}")
            if action in options.keys():
                if action == "Q":
                    Bank.user_session = "Q"
                return action
            print(invalid("choice"))
        
    @classmethod
    def create_new_account_type(self, acct_type):
        setattr(Bank.user, acct_type.lower(), 0)
        Bank.update_data()
        print(f"Congratulations on opening your new {acct_type}.")
        return 
    
    @classmethod
    def show_account_not_active_info(self):
        accts_to_reactivate = []

        if Bank.user.checking < 0:
            accts_to_reactivate.append(["checking", Bank.user.checking])

        if Bank.user.savings < 0:
            accts_to_reactivate.append(["savings", Bank.user.savings])

        acct_info = '\n'.join([f'Your current {acct[0]} balance is {acct[1]}' for acct in accts_to_reactivate])
        print(f"Your account is deactivated and cannot currently be accessed.\nIn order to use your account you must deposit enough money to become solvent.\n{acct_info}. Please add money to bring all accounts to a minimum balance of (0) zero.")

        return accts_to_reactivate

    @classmethod
    def reactivate_accounts(self, accts_to_reactivate):
        user_choice = None
        max_deposit = 100

        while len(accts_to_reactivate) > 0 and user_choice != "Q":
            curr_acct_balance = getattr(Bank.user, accts_to_reactivate[0][0])
            min_deposit = abs(1 - curr_acct_balance)
            print(f"\nLet's fix your {accts_to_reactivate[0][0]} account. The minimum amount you must deposit is {min_deposit}")
            deposit_amt = 0
            while deposit_amt < min_deposit or deposit_amt > max_deposit:
                new_amt = input("How much would you like to deposit or 'Q' to quit: => ")
                if new_amt.isdigit() and int(new_amt) <= max_deposit and int(new_amt) >= min_deposit:
                    deposit_amt = int(new_amt)
                elif new_amt == "Q":
                    Bank.user_session = "Q"
                    return
                else:
                    print(invalid("number"))
            updated_amount = abs(curr_acct_balance + deposit_amt)
            setattr(Bank.user, accts_to_reactivate[0][0], updated_amount)
            accts_to_reactivate.pop(0)

        Bank.user.overdraft_count = 0
        Bank.user.active = True
        Bank.update_data()
        print("Thank you for reactivating your account!")





