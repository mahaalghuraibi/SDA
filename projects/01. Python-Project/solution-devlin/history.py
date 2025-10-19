import csv
import datetime
now = datetime.datetime.now().replace(microsecond=0)
date_format = "%Y-%m-%d %H:%M:%S"

############################# HELPER FUNCTION #############################################
def show_dict_items(dictionary):
    return "\n".join([ f"{key}: {val}" for key, val in dictionary.items()])+":: User Choice => "

############################# HISTORY CLASS #############################################

# - Create an account log that collects historical data about all transactions that occur.
# - Allow a user to view their entire transaction log
# - Allow a user to select one specific transaction to view and display extra detail

# TRANSACTIONS TO TRACK



class HistoryEntry():
    LOOKUP = {
        "signup":            "SIGNUP",
        "login":             "LOGIN",
        "create-checking":   "CREATE CHECKING",
        "create-savings":    "CREATE SAVINGS",
        "balance":           "CHECK BALANCE",
        "deposit":           "DEPOSIT",
        "withdraw":          "WITHDRAW",
        "transfer":          "TRANSFER INITIATED",
        "trans-with-int":    "WITHDRAW (INTERNAL TRANSFER)",
        "trans-with-ext":    "WITHDRAW (EXTERNAL TRANSFER)",
        "trans-dep-int":     "DEPOSIT (INTERNAL TRANSFER)",
        "trans-dep-ext":     "DEPOSIT (EXTERNAL TRANSFER)",
        "deactivate":        "ACCOUNT DEACTIVATED",
        "reactivate":        "ACCOUNT REACTIVATED",
    }


    def __init__(self, id="", user_id="", date="", action="", account_type="", transfer_to="", transfer_from="", amount="", starting_balance="", ending_balance="" ):
    
        if not id:
            History.id +=1
            self.id = History.id
        else:
            self.id = int(id)

        self.user_id          = int(user_id)
        self.date             = datetime.datetime.strptime(date, date_format)
        self.action           = action
        self.account_type     = account_type
        self.transfer_to      = transfer_to
        self.transfer_from    = transfer_from
        self.amount           = amount
        self.starting_balance = starting_balance
        self.ending_balance   = ending_balance

    def __str__(self):
        lines = []
        for key, value in self.__dict__.items():
            if value or value == 0:
                lines.append(f"{key}: {value}")
        return "\n".join(lines)

class History():
    fieldnames = ['id', 'user_id', 'date', 'account_type', 'action', 'transfer_to', 'transfer_from', 'amount', 'starting_balance', 'ending_balance']
    filename = "./history.csv"
    id = 0
    history_entries   = []
    curr_user_entries = []

    def __init__(self):
        pass

    @classmethod
    def add_transaction_entry(cls, new_entry):
        try:
            with open(History.filename, "a+") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=History.fieldnames)
                writer.writerow(new_entry.__dict__)
        except csv.Error as e:
            print(e)

    @classmethod
    def load_history(cls):
        try: 
            with open(History.filename, "r") as file:
                history_entries = csv.DictReader(file)
                for row in history_entries:
                    history_entry = HistoryEntry(id=row["id"], user_id=row["user_id"], date=row["date"], action=row["action"], account_type=row["account_type"], transfer_to=row["transfer_to"], transfer_from=row["transfer_from"], amount=row["amount"], starting_balance=row["starting_balance"], ending_balance=row["ending_balance"] )
                    if history_entry.id >= History.id:
                        History.id = history_entry.id
                    History.history_entries.append(history_entry)
        except csv.Error as e:
            print(e)

    @classmethod
    def get_user_history(cls, user, acct):
        user_history_entries = []
        for entry in History.history_entries:
            if entry.user_id == user.id and entry.account_type.lower() == acct.lower():
                user_history_entries.append(entry)
        if len(user_history_entries) > 0:
            print("These are your most recent transactions:\n")
            options = { "1": "See details about an entry", "2": "Return to the main menu."}
            user_choice = None
            while user_choice not in options:
                for item in user_history_entries:
                    print(f""" 
                        ID:               {item.id}
                        Date:             {item.date}
                        Transaction:      {item.action}
                        Account Type:     {item.account_type}
                    \n""")
                user_choice = input(f"Would you like to:\n{show_dict_items(options)}")

                if user_choice == "1":
                    cls.display_transaction_detail_for_user(user, user_history_entries)
                if user_choice == "2":
                    return
                if user_choice not in options:
                    print("Please choose a valid option.")
        else:
            print("You do not have any transactions yet.")
        

    @classmethod
    def display_transaction_detail_for_user(cls, user, user_history_entries):
        transaction_id = None
        detail = None
    
        while not detail and transaction_id != "Q":
            transaction_id = input("\nPlease enter the id of the transaction you would like to see more details for or press 'Q' to quit.\n")

            if transaction_id == "Q":
                return
            
            if transaction_id.isdigit():
                for entry in user_history_entries:
                    if entry.user_id == user.id and entry.id == int(transaction_id):
                        print(entry)
            else:
                print("Please enter a valid number.\n")
