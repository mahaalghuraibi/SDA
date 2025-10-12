
############################# HELPER FUNCTION #############################################
def show_dict_items(dictionary):
    return "\n".join([ f"{key}: {val}" for key, val in dictionary.items()])+":: User Choice => "

def invalid(item):
    options = { "number": "\nPlease choose a valid amount.", "choice": "\nPlease choose a valid option." }
    return options[item]

############################# TRANSACTIONS CLASS #############################################

class Transactions():
    user = None
    user_session = None
    update_accounts = None
    find_acct = None
    fee = 35

    def __init__(self):
        pass

    @classmethod
    def get_balance(cls, acct_type):
        balance = getattr(Transactions.user, acct_type)
        print(f"Your current {acct_type} account balance is: {balance}")

    @classmethod
    def withdraw(cls, acct, transfer=False):
        will_overdraft = False
        acct = acct.lower()
        withdraw_amt = None

        # CHECK USER WITHDRAW WINDOW
        curr_acct_balance = getattr(Transactions.user, acct.lower())
        maximum = cls.calculate_max_withdraw(curr_acct_balance)
        if maximum == 0:
            print("\nApologies, but you are unable to withdraw money at this time due to insufficient funds.\nPlease deposit more money into your account.")
            return "Q"

        # REQUEST WITHDRAW AMOUNT
        while type(withdraw_amt) is not int and withdraw_amt != "Q":
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
                print(invalid("number"))
                withdraw_amt = None

        # CALCULATE OVERDRAFT / DEACTIVATION / PROMPT PROCEED
        proceed_msg = f"\nThe following transaction will {'transfer' if transfer else 'withdraw'} {withdraw_amt} from your {acct} account."
        if curr_acct_balance - withdraw_amt < 0:
            will_overdraft = True
        if will_overdraft:
            proceed_msg += "\nThis transaction will result in an overdraft fee of $35."
        if will_overdraft and Transactions.user.overdraft_count + 1 >= 2:
            proceed_msg += "\nAdditionally your account will be deactivated due to excess overdraft."
        
        # CONFIRM USER WANTS TO PROCEED
        proceed_options = {"Y": "Yes", "Q": "Quit\n"}
        proceed_choice = None
        while proceed_choice not in proceed_options:
            proceed_choice = input(f"{proceed_msg}\nWould you like to proceed with the {'transfer' if transfer else 'withdraw'}?\n{show_dict_items(proceed_options)}")
            if proceed_choice == "Q":
                Transactions.user_session = "Q"
                return "Q"
            if proceed_choice not in proceed_options:
                print(invalid("choice"))
            
        # UPDATE USER AND BANK ACCT INFO
        update_amt = curr_acct_balance - withdraw_amt

        if will_overdraft:
            update_amt = update_amt - Transactions.fee
            Transactions.user.overdraft_count += 1

        if Transactions.user.overdraft_count >= 2:
            Transactions.user.active = False

        setattr(Transactions.user, acct, update_amt)
        Transactions.update_accounts()

        print(f"\nThe {'transfer' if transfer else 'withdraw'} amount of ${withdraw_amt} from your {acct} was successful with a resulting balance of ${update_amt}")
        return withdraw_amt

        
    @classmethod
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
    def deposit(cls, acct, transfer=False, internal=True, deposit_amt=0, ext_acct=None, ext_acct_type=None):
        acct = acct.lower()

        if not transfer:
            while (type(deposit_amt) is not int or deposit_amt <= 0) and deposit_amt != "Q":
                deposit_amt = input("Please enter the amount you would like to deposit =>  ")
                
                if deposit_amt == "Q":
                    Transactions.user_session = "Q"
                    return
                    
                if not deposit_amt.isdigit():
                    print(invalid("number"))
                    deposit_amt = 0
                    continue
                
                deposit_amt = int(deposit_amt)
                if deposit_amt <= 0:
                    print(invalid("number"))
        

        if internal:
            curr_amt = getattr(Transactions.user, acct)
            update_amt = curr_amt + deposit_amt
            setattr(Transactions.user, acct, update_amt)
            print(f"\n{deposit_amt} has been added to your {acct} with a resulting balance of {update_amt}")


        if not internal:
            curr_amt = getattr(ext_acct, ext_acct_type)
            update_amt = curr_amt + deposit_amt
            setattr(ext_acct, ext_acct_type, update_amt)
            print(f"\n{deposit_amt} has been added to acct number {ext_acct.id}'s {ext_acct_type} with a resulting balance of {update_amt}")

        Transactions.update_accounts()
        return
                
    @classmethod
    def transfer(cls, acct):
        acct = acct.lower()
        trans_type = None
        opp_acct = "savings" if acct == "checking" else "checking"
        ext_acct = None
        account_type_to_transfer_to = None

        # TRANSFER OPTIONS -> 
        # IF USER HAS BOTH ACCT TYPES -> CAN TRANSFER FROM ONE TO OTHER
        if type(cls.user.checking) == int and type(cls.user.savings):
            trans_type_options = { "1": f"Transfer from {acct} to {opp_acct}", "2": f"Transfer from {acct} to an external account.", "Q": "Quit\n" }
            trans_type_choice = None
            while trans_type_choice not in trans_type_options and trans_type_choice != "Q":
                trans_type_choice = input(f"\nWhich transfer would you like to do?\n{show_dict_items(trans_type_options)}")

                if trans_type_choice == "1":
                    trans_type = "internal"
                if trans_type_choice == "2":
                    trans_type = "external"
                if trans_type_choice == "Q":
                    Transactions.user_session = "Q"
                    return
                if trans_type_choice not in trans_type_options:
                    invalid("choice")

        # ELSE USER CAN ONLY TRANSFER FROM ONE ACCOUNT TO ANOTHER ACCOUNT
        if trans_type == "external":
            valid_ext_id = False
            while not valid_ext_id:
                ext_acct = input("\nPlease enter the id of the account you would like to transfer to or 'Q' to quit. => ")

                # STR(ID) IS A NUMBER / SEARCH IF IT IS IN THE DB (CSV)
                if ext_acct.isdigit():
                    ext_acct = int(ext_acct)
                    account_found = cls.find_acct(ext_acct)


                    # ACCOUNT FOUND WITH ID
                    if account_found:
                        valid_ext_id = True
                        ext_acct = account_found

                        print(ext_acct, "188 account found!", account_found.checking, isinstance(account_found.checking, int), type(account_found.savings), isinstance(account_found.savings, int))

                        # BOTH -> REQUIRES CHOICE!
                        
                        if type(account_found.checking) == int and type(account_found.savings) == int:
                            account_choice_options = { "1": "Checking", "2": "Savings", "Q": "Quit" }
                            account_choice = None
                            while account_choice not in account_choice_options and account_choice != "Q":
                                account_choice = input(f"\nPlease choose the account type you would like to transfer to.\n{show_dict_items(account_choice_options)}")
                                if account_choice == "Q":
                                    cls.user_session = "Q"
                                    return
                                if account_choice == "1":
                                    account_type_to_transfer_to = "checking"
                                if account_choice == "2":
                                    account_type_to_transfer_to = "savings"
                                if account_choice not in account_choice_options:
                                    invalid("choice")

                        # ONLY CHECKING
                        elif type(account_found.checking) == int and type(account_found.savings) == bool:
                            account_type_to_transfer_to = "checking"
                        # ONLY SAVINGS
                        elif type(account_found.savings) == int and type(account_found.checking) == bool:
                            account_type_to_transfer_to = "savings"
                
                if ext_acct == "Q":
                    cls.user_session = "Q"
                    return
        
        # ASK HOW MUCH TO TRANSFER / COMPLETE THIS STEP
        amount_to_deposit = Transactions.withdraw(acct, transfer=True)

        # RETURN IF 'Q' OR NOT ACTUAL AMOUNT
        if type(amount_to_deposit) is not int or amount_to_deposit == "Q":
            Transactions.user_session = "Q"
            return
    
        # DEPOSIT INTO INTERNAL
        if trans_type == "internal":
            Transactions.deposit(opp_acct, transfer=True, internal=True, deposit_amt=amount_to_deposit)
            return


        # DEPOSIT INTO EXTERNAL
        if trans_type == "external":
            print("231", ext_acct, account_type_to_transfer_to)
            Transactions.deposit(acct, transfer=True, internal=False, deposit_amt=amount_to_deposit, ext_acct=ext_acct, ext_acct_type=account_type_to_transfer_to)
            return

        print("Transfer complete!\n")
        return



    



