import bank

############################# HELPER FUNCTION #############################################
def show_dict_items(dictionary):
    return "\n".join([ f"{key}: {val}" for key, val in dictionary.items()])+":: User Choice => "

############################# TRANSACTIONS CLASS #############################################

class Transactions():

    def __init__(self):
        pass

    @classmethod
    def withdraw(self, user, acct, transfer):
        fee = 35
        withdraw_amt = None
        will_overdraft = False
        proceed_with_action = False
        acct = acct.lower()
        opposite_acct = "savings" if acct == "checking" else "checking"
        curr_acct_balance = getattr(user, acct.lower())
        maximum = self.calculate_max_withdraw(user, curr_acct_balance)

        if maximum == 0:
            print("\nApologies, but you are unable to withdraw money at this time due to insufficient funds. Please deposit more money into your account.")
            return "Q"

        while withdraw_amt != "Q" and type(withdraw_amt) is not int:
            try:
                withdraw_amt = input(f"\nPlease enter the amount you would like to {'transfer' if transfer else 'withdraw'} from your {acct} account.\nYour current balance is {curr_acct_balance}. The maximum amount of money you may {'transfer' if transfer else 'withdraw'} is {maximum}\n:: Withdraw Amount =>  ")
                withdraw_amt = int(withdraw_amt)

                if withdraw_amt < 0 or withdraw_amt > maximum:
                    print(f"\nPlease choose a number greater than 0 and less than {maximum}.")
                    withdraw_amt = None

                if withdraw_amt == "Q":
                    return "Q"
                
            except ValueError as e:
                print(e)
                print("Please provide an actual number.")
                withdraw_amt = None

        while proceed_with_action not in [True, "Q", "Y"]:
            proceed_options = {"Y": "Yes", "Q": "Quit\n"}
            intial_input = f"\nThe following transaction will decuct {withdraw_amt} from your {acct}{f' and initiate a transfer. This cannot be cancelled once you confirm.' if transfer else '.'}"
            if withdraw_amt == "Q":
                return "Q"
            if curr_acct_balance - withdraw_amt < 0:
                will_overdraft = True
            if will_overdraft:
                intial_input += "\nThis withdrawal transaction will result in an overdraft fee of $35."
            if will_overdraft and user.overdraft_count + 1 >= 2:
                intial_input += "\nAdditionally your account will be deactivated due to excess overdraft."
            
            intial_input += f"\nPlease confirm the transaction with\n{show_dict_items(proceed_options)}"
            proceed = input(intial_input)
            if proceed == "Y":
                proceed_with_action = True
            if proceed == "Q":
                return "Q"
            

        # UPDATE USER AND BANK ACCT INFO
        if proceed_with_action:
            update_amt = curr_acct_balance - withdraw_amt

            if will_overdraft and update_amt < 0:
                update_amt = update_amt - fee
                user.overdraft_count += 1

            if user.overdraft_count >= 2:
                user.active = False

            setattr(user, acct, update_amt)

            # UPDATE BANKING DATA
            for c in bank.Bank.customers:
                if c.id == user.id:
                    c.checking = user.checking
                    c.savings = user.savings
                    c.active = user.active
                    c.overdraft_count = user.overdraft_count

            bank.Bank.update_data()

            print(f"\nThe withdraw amount of ${withdraw_amt} from your {acct} was successful.\nThe resulting balance is ${update_amt}")

        # RETURN UPDATED USER
        return user
        

    def calculate_max_withdraw(self, curr_acct_balance):
        if curr_acct_balance > 35:
            return 100
        if curr_acct_balance <= -65:
            return 0
        if curr_acct_balance > 0:
            return curr_acct_balance + 65
        if curr_acct_balance <= 0:
            return 65 - abs(curr_acct_balance)


    @classmethod
    def deposit(self, user, acct, reactivate, add_amt, transfer, external):
        acct = acct.lower()
        deposit_amt = add_amt if transfer else None
        external_acct = None
        external_acct_choice = None
        external_acct_choices = []

        # SET INPUT MSG:
        if not transfer:
            input_msg = ""
            if reactivate:
                input_msg += f"You must deposit at least {abs(getattr(user, acct))} to into your {acct} account. How much would you like to deposit?\n:: Deposit amount => "
            else:
                input_msg += f"\nHow much would you like to deposit into your {acct} account?\n:: Deposit amount => "
    
            # GET DEPOSIT AMOUNT
            while deposit_amt != "Q" and type(deposit_amt) is not int:
                deposit_amt = input(input_msg)
                try:
                    if deposit_amt == "Q":
                        return "Q"
                    deposit_amt = int(deposit_amt)
                except ValueError:
                    print("\n**Please enter a real number**")
        
        if transfer and external:
            acct_id_validated = False
            acct_id_input = None
            while acct_id_input != "Q" and not acct_id_validated and type(acct_id_input) is not int :
                try:
                    acct_id_input = input("\nPlease enter the account number of the account you would like to transfer to.\n:: User Input => ")
                    acct_id_input = int(acct_id_input)

                    for c in bank.Bank.customers:
                        if c.id == acct_id_input:
                            acct_id_validated = True
                            external_acct = c
                            if type(c.checking) == int:
                                external_acct_choices.append("checking")
                            if type(c.savings) == int:
                                external_acct_choices.append("savings")

                    
                    if not acct_id_validated:
                        print("Please enter a valid account number to transfer to.")
                        acct_id_input = None

                except ValueError as e:
                    print("\n**Please enter a real number.**")

            if len(external_acct_choices) == 2:
                external_acct_input = None
                while external_acct_input not in ["1", "2", "Q"]:
                    external_acct_input = input(f"\nPlease choose the account to transfer to.\n(1) Checking.\n(2) Savings\n(Q) Quit\n:: User Choice => ")
                    if external_acct_input == "1":
                        external_acct_choice = 'checking'
                    if external_acct_input == "2":
                        external_acct_choice = 'savings'
                    if external_acct_input == "Q":
                        return "Q"
            else:
                external_acct_choice = external_acct_choices[0]
            

        if not external:
            curr_amt = getattr(user, acct)
            update_amt = curr_amt + deposit_amt
            setattr(user, acct, update_amt)
            for c in bank.Bank.customers:
                if c.id == user.id:
                    c.checking = user.checking
                    c.savings = user.savings

        if external:
            curr_amt = getattr(external_acct, external_acct_choice)
            update_amt = curr_amt + add_amt
            for c in bank.Bank.customers:
                if c.id == external_acct.id:
                    setattr(c, external_acct_choice, update_amt)

        bank.Bank.update_data()

        print(f"\nThe {'transfer' if transfer else 'deposit'} of ${deposit_amt} into { f'account number {external_acct.id}' if external else f'your {acct}'} was successful.\nThe resulting balance is ${update_amt}")

        # RETURN UPDATED USER
        return user
                
    @classmethod
    def transfer(self, user, acct):
        reactivate = False
        transfer = True
        external = False
        acct = acct.lower()
        opposite_acct = "savings" if acct == "checking" else "checking"

        action= None
        options = ["Q", "1", "2"]
        while action not in options:
            action = input(f"\nWhich transfer would you like to do?\n(1) From your {acct} account to your {opposite_acct} account?\n(2) From your {acct} account to an external account?\n(Q) Quit\n:: User Choice => ")

            if action == "Q":
                return "Q"
            
            if action not in options:
                print("\n**Invalid option, please try again.**")
                action = None

        if action == "1" or action == "2":
            previous_amt = getattr(user, acct)
            user = Transactions.withdraw(user, acct, transfer)

            if user == "Q":
                return "Q"
            
            if action == "2":
                external = True
        
            new_amt = getattr(user, acct)
            add_amt = previous_amt - new_amt

            user = Transactions.deposit(user, opposite_acct, reactivate, add_amt, transfer, external)

            if user == "Q":
                return "Q"

        return user