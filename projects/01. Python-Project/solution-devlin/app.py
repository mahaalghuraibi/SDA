import os
import bank
import customer
import seed

############################# HELPER FUNCTION #############################################
def show_dict_items(dictionary):
    return "\n".join([ f"{key}: {val}" for key, val in dictionary.items()])+":: User Choice => "

############################# APPLICATION START #############################################
def app():
    if not os.path.exists("./bank.csv"):
        seed.generate_seed_data()    

    # state variables
    bank.Bank.load_data()
    user_session = None
    user = None

    # START SESSION - USER or NO USER??
    while user_session != "Q":
        
        # NO USER => SIGNUP or LOGIN
        while user == None and user_session != "Q":
            non_user_options = {"1": "Create an account.", "2": "Login", "Q": "Exit\n"}
            non_user_choice = None

            while non_user_choice not in non_user_options.keys():
                non_user_choice = input(f"Welcome to Gotham Banking.\n\nPlease select one of the following options.\n{show_dict_items(non_user_options)}")

                if non_user_choice == "1":
                    user = bank.Bank.signup()

                if non_user_choice == "2":
                    user = bank.Bank.login()

                if non_user_choice not in non_user_options.keys():
                    print("\n**Please choose a valid option**\n")

                if non_user_choice == "Q" or user == "Q":
                    user_session = "Q"

        # USER => CREATE ONE NEW ACCT or HAS BOTH ACCOUNT TYPES
        while isinstance(user, customer.Customer) and user_session != "Q":
            activated_user_options = {"1": "Checking", "2": "Savings", "Q": "Exit\n"}
            deactivated_user_options = {"Y": "Yes", "Q": "Exit\n"}

            # USER ACCOUNT DEACTIVATED
            if not user.active:
                user_choice = None

                while user_choice not in deactivated_user_options.keys():
                    accts_to_reactivate = bank.Bank.show_account_not_active_info(user)
                    user_choice = input(f"Would you like to reactivate your account?\n{show_dict_items(deactivated_user_options)}")

                    if user_choice == "Y":
                        user = bank.Bank.reactivate_account(user, accts_to_reactivate)

                    if user_choice not in deactivated_user_options.keys():
                        print("**Please choose a valid option**")

                    if user_choice == "Q" or user == "Q":
                        user_session = "Q"
                
            # BOTH ACCOUNTS => ACCESS EITHER
            if type(user.checking) is int and type(user.savings) is int and user.active:
                user_choice = None
                
                while user_choice not in activated_user_options.keys() and user_session != "Q" or user_choice == "Y":
                    user_choice = input(f"\nWhich account would you like to access?\n{show_dict_items(activated_user_options)}")

                    if user_choice == "1" or user_choice == "2": 
                        user = bank.Bank.access_existing_account(user, activated_user_options[user_choice])

                    if user_choice not in activated_user_options.keys() and user_choice != "Y":
                        print("\n**Please choose a valid option**\n")

                    if user_choice == "Q" or user == "Q":
                        user_session = "Q"

            # ONE ACCOUNT => ACCESS ONE or CREATE OTHER
            else:
                user_choice = None

                while user_choice not in activated_user_options.keys() and user_session != "Q" and user_choice != "Q" or user_choice == "Y":
                    acct_open     = "1" if type(user.checking) is int else "2"
                    acct_not_open = "1" if type(user.savings)  is int else "2"
                    user_choice   = input(f"\nWould you like to:\n1: Access Your {activated_user_options[acct_open]} Account\n2: Open a {activated_user_options[acct_not_open]} Account\nQ: Exit\n:: User Choice => ")

                    if user_choice == "1":
                        user = bank.Bank.access_existing_account(user, activated_user_options[acct_open])
                        user_choice = bank.Bank.ask_another_transaction("Would you like another transaction?")

                    if user_choice == "2":
                        user = bank.Bank.create_new_account_type(user, activated_user_options[acct_not_open])
                        user_choice = bank.Bank.ask_another_transaction("Would you like another transaction?")

                    if user_choice not in activated_user_options.keys() and user_choice != "Y":
                        print("\n**Please choose a valid option**\n")

                    if user_choice == "Q" or user == "Q":
                        user_session = "Q"

    # Exit / Goodbye!  
    print("Thank you for visiting Gotham Bank! Have a nice day!")

# Start main application #
app()