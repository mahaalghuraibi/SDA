import os
import seed as seed
from bank import Bank
from customer import Customer
from history import History
import datetime
now = datetime.datetime.now().replace(microsecond=0)

### TO-DO
## REFACTOR TRANSFERS
## ADD HISTORY ENTRIES
## DISPLAY FULL HISTORY ENTRIES LIST
## DISPLAY DETAIL / QUIT

############################# HELPER FUNCTION #############################################
def show_dict_items(dictionary):
    return "\n".join([ f"{key}: {val}" for key, val in dictionary.items()])+":: User Choice => "

############################# APPLICATION START #############################################
def app():
    # ENSURE BANK.CSV FILE EXISTS / IS SEEDED
    if not os.path.exists(Bank.filename):
        seed.generate_bank_seed_data(Bank.filename, Bank.fieldnames) 
    if not os.path.exists(History.filename):
        seed.generate_history_seed_data(History.filename, History.fieldnames)

    # LOAD BANK ACCOUNTS and HISTORY ENTRIES
    Bank.load_accounts()
    History.load_history()

    # START SESSION
    while Bank.user_session != "Q":
        
        # NO USER => SIGNUP or LOGIN
        while Bank.user == None and Bank.user_session != "Q":
            non_user_options = {"1": "Create an account.", "2": "Login", "Q": "Exit\n"}
            non_user_choice = None

            while non_user_choice not in non_user_options.keys():
                non_user_choice = input(f"Welcome to Gotham Banking.\n\nPlease select one of the following options.\n{show_dict_items(non_user_options)}")

                if non_user_choice == "1":
                    Bank.signup()

                if non_user_choice == "2":
                    Bank.login()

                if non_user_choice == "Q":
                    Bank.user_session = "Q"

                if non_user_choice not in non_user_options.keys():
                    print("\n**Please choose a valid option**\n")


        # USER => CREATE NEW ACCT, HAS BOTH ACCOUNT TYPES, ACCT DEACTIVATED
        while isinstance(Bank.user, Customer) and Bank.user_session != "Q":
            activated_user_options = {"1": "Checking", "2": "Savings", "Q": "Exit\n"}
            deactivated_user_options = {"Y": "Yes", "Q": "Exit\n"}


            # USER ACCOUNT DEACTIVATED
            if not Bank.user.active:
                user_choice = None

                while user_choice not in deactivated_user_options.keys():
                    accts_to_reactivate = Bank.show_account_not_active_info()
                    user_choice = input(f"Would you like to reactivate your account?\n{show_dict_items(deactivated_user_options)}")

                    if user_choice == "Y":
                        Bank.reactivate_accounts(accts_to_reactivate)

                    if user_choice == "Q":
                        Bank.user_session = "Q"

                    if user_choice not in deactivated_user_options.keys():
                        print("**Please choose a valid option**\n")

                
            # BOTH ACCOUNTS => ACCESS EITHER
            if type(Bank.user.checking) is int and type(Bank.user.savings) is int and Bank.user.active:
                user_choice = None
                
                while user_choice not in activated_user_options.keys() and Bank.user_session != "Q":
                    user_choice = input(f"\nWhich account would you like to access?\n{show_dict_items(activated_user_options)}")

                    if user_choice == "1" or user_choice == "2" and Bank.user_session != "Q": 
                        Bank.access_existing_account(activated_user_options[user_choice])
                    
                    if user_choice == "Q":
                        Bank.user_session = "Q"
                        return 

                    if user_choice not in activated_user_options.keys():
                        print("\n**Please choose a valid option**\n")

            # ONE ACCOUNT => ACCESS ONE or CREATE OTHER
            else:
                user_choice = None

                # FIND WHICH ACCT USER HAS
                while user_choice not in activated_user_options.keys() and Bank.user_session != "Q":
                    acct_open     = "1" if type(Bank.user.checking) is int else "2"
                    acct_not_open = "1" if type(Bank.user.savings)  is int else "2"
                    options       = { "1": f"Access your {activated_user_options[acct_open]} account.", "2": f"Open a {activated_user_options[acct_not_open]} account.", "Q": "Exit\n"}
                    user_choice   = input(f"\nWould you like to:\n{show_dict_items(options)}")

                    if user_choice == "1":
                        Bank.access_existing_account(activated_user_options[acct_open])
                        Bank.ask_another_transaction()

                    if user_choice == "2":
                        Bank.create_new_account_type(activated_user_options[acct_not_open])
                        Bank.ask_another_transaction()

                    if user_choice == "Q":
                        Bank.user_session = "Q"

                    if user_choice not in activated_user_options.keys():
                        print("\n**Please choose a valid option**\n")

    # Exit / Goodbye!  
    print("Thank you for visiting Gotham Bank! Have a nice day!")

# Start main application #
app()