import csv
import transaction
import customer

############################# HELPER FUNCTION #############################################
def show_dict_items(dictionary):
    return "\n".join([ f"{key}: {val}" for key, val in dictionary.items()])+":: User Choice => "


############################# BANK CLASS #####################################################
class Bank():
    acct_id = 0
    customers = []
    fieldnames = ['id', "first_name", 'last_name', "password", "checking", "savings", "active", "overdraft_count"]

    def __init__(self):
        pass

    @classmethod
    def load_data(self):
        try: 
            with open("./bank.csv", "r") as file:
                contents = csv.DictReader(file)
                for row in contents:
                    # convert: id, checking, savings, active, overdraft_count to non-string values
                    row['id'] = int(row["id"])
                    row["checking"] = False if row["checking"] == "False" else int(row["checking"])
                    row["savings"]  = False if row["savings"]  == "False" else int(row["savings"])
                    row["active"]   = True  if row["active"]   == "True"  else False
                    row["overdraft_count"] = int(row["overdraft_count"])
                    row = customer.Customer(row["id"], row["first_name"], row["last_name"], row["password"], row["checking"], row["savings"], row["active"], row["overdraft_count"])
                    self.customers.append(row)
                    if row.id >= Bank.acct_id:
                        Bank.acct_id = row.id
        except csv.Error as e:
            print(e)
    
    @classmethod
    def update_data(self):
        with open("./bank.csv", 'w', newline='') as csvfile:
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
        user_id = None
        user_pass = None

        while not validated and (user_id != "Q" or user_pass != "Q"):
            # GET USER INFO: ID and PASSWORD
            user_id = input("\nPlease provide your account id or 'Q' to quit.\n:: Account ID => ")
            if user_id == "Q":
                return "Q"
            user_pass = input("\nPlease provide your account password 'Q' to quit.\n:: Account Password => ")
            if user_pass == "Q":
                return "Q"
            
            # VALIDATE
            for acct in self.customers:
                if str(acct.id) == user_id and user_pass == acct.password:
                    validated = True
                    print(f"\nWelcome back, {acct.first_name} {acct.last_name}.")
                    return acct
            if not validated:
                print("\nPlease enter the correct credentials to login or 'Q' to quit.")

        return None

    @classmethod
    def signup(self):
        new_id = Bank.acct_id + 1
        new_user = customer.Customer(new_id)

        # GET/SET USER INFO
        print("\nWe're delighted you would like to join us. Please provide the following information to start an account:")
        new_user.first_name = input("\nPlease provide your legal first name:\n:: User First Name => ")
        new_user.last_name  = input("\nPlease provide your legal last name:\n:: User Last Name => ")
        new_user.password   = input("\nPlease provide a password with at least 5 characters:\n:: User Password => ")
        
        # GET ACCT CHOICE
        acct_options_dict = {"1": "checking", "2": "savings", "Q": "Exit"}
        acct_choice = None
        while acct_choice not in acct_options_dict.keys():
            acct_choice = input(f"\nPlease choose an account to open:\n{show_dict_items(acct_options_dict)}")
            if acct_choice == "Q":
                return "Q"
            if acct_choice not in acct_options_dict.keys():
                print("**Please choose a valid option.**")

        # CREATE SUCCESSFUL => SET ACCT TO 0, SET ID, UPDATE BANK DATA
        setattr(new_user, acct_options_dict[acct_choice], 0)
        Bank.acct_id += 1 # successful acct creation => update id count
        Bank.customers.append(new_user)
        Bank.update_data()
        print(f"Thank you, {new_user.first_name} {new_user.last_name}, for joining Gotham Bank!! Welcome!")
        return new_user
        
    @classmethod
    def access_existing_account(self, user, acct_type):
        account_actions_dict = { "1": "Deposit", "2": "Withdraw", "3": "Transfer", "4": "Check Balance", "Q": "Exit\n" }
        acct_type = acct_type.lower()
        action = None

        while action not in account_actions_dict.keys() and action != "Q" or action == "Y":
            action = input(f"\nWhat would you like to do in your {acct_type}?\n{show_dict_items(account_actions_dict)}")
            if action == "1":
                user = transaction.Transactions.deposit(user, acct_type)
            if action == "2":
                user = transaction.Transactions.withdraw(user, acct_type)
            if action == "3":
                user = transaction.Transactions.transfer(user, acct_type)
            if action == "4":
                balance = getattr(user, acct_type)
                print(f"Your current {acct_type} account balance is: {balance}")
            if action == "Q" or user == "Q":
                return user
            if action not in account_actions_dict.keys():
                print("\n**Invalid choice. Please choose one of the 5 options.**\n")

        return user

    @classmethod
    def ask_another_transaction(self, msg):
        another_transaction_options = { "Y": "Yes", "Q": "Exit\n" }
        another_transaction_action = None
        while another_transaction_action not in another_transaction_options.keys() and another_transaction_action != "Q":
            another_transaction_action = input(f"\n{msg}\n{show_dict_items(another_transaction_options)}")
            if another_transaction_action not in another_transaction_options.keys():
                print("\n**Invalid choice. Please choose one of the 3 options.**\n")
            return another_transaction_action
        
    @classmethod
    def create_new_account_type(self, user, acct_type):

        setattr(user, acct_type.lower(), 0)
        for c in Bank.customers:
            if c.id == user.id:
                c.checking = user.checking
                c.savings = user.savings
        Bank.update_data()

        print(f"Congratulations on opening your new {acct_type}.")
        return user
    
    @classmethod
    def show_account_not_active_info(self, user):
        accts_to_reactivate = []
        if user.checking < 0:
            accts_to_reactivate.append(["checking", user.checking])
        if user.savings < 0:
            accts_to_reactivate.append(["savings", user.savings])
        acct_info = '\n'.join([f'Your current {acct[0]} balance is {acct[1]}' for acct in accts_to_reactivate])
        print(f"Your account is deactivated and cannot currently be accessed.\nIn order to use your account you must deposit enough money to become solvent.\n{acct_info}. Please add money to bring all accounts to a minimum balance of (0) zero.")
        return accts_to_reactivate

    @classmethod
    def reactivate_account(self, user, accts_to_reactivate):
        user_choice = None

        while len(accts_to_reactivate) > 0 and user_choice != "Q":
            curr_acct_to_reactivate = accts_to_reactivate[0]
            print(f"\nLet's fix your {curr_acct_to_reactivate[0]} account")
            user = transaction.Transactions.deposit(user, curr_acct_to_reactivate[0], reactivate=True)
            if user == "Q":
                return "Q"
            if isinstance(user, customer.Customer):
                curr_acct = getattr(user, curr_acct_to_reactivate[0])
            if curr_acct >= 0:
                accts_to_reactivate.pop(0)
                    
        if len(accts_to_reactivate) == 0:
            for c in Bank.customers:
                if c.id == user.id:
                    c.checking = user.checking
                    c.savings = user.savings
                    if c.checking >= 0 and c.savings >= 0:
                        c.overdraft_count = 0
                        c.active = True
                        user.overdraft_count = 0
                        user.active = True
            Bank.update_data()
            print("Thank you for reactivating your account!")

        return user





