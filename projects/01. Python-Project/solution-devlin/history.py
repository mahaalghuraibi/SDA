import csv

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
        "1":    "SIGNUP",
        "2":    "LOGIN",
        "3":    "CHECK BALANCE",
        "4":    "DEPOSIT",
        "5":    "WITHDRAW",
        "6":    "TRANSFER (INTERNAL -> WITHDRAW)",
        "7":    "TRANSFER (INTERNAL -> DEPOSIT)",
        "8":    "TRANSFER (EXTERNAL -> WITHDRAW -> TO: ",
        "9":    "TRANSFER (EXTERNAL -> DEPOSIT -> FROM: ",
        "10":   "ACCOUNT DEACTIVATED",
        "11":   "ACCOUNT REACTIVATED",
    }

    # FIX THIS!!
    def __init__(self, entry_type, acct):
        self.id               = int(acct["id"])
        self.user_id          = int(acct["user_id"])
        self.account_type     = acct["account_type"]
        self.transction_type  = acct["transaction_type"]
        self.amount           = int(acct["amount"])
        self.starting_balance = int(acct["starting_balance"])
        self.ending_balance   = int(acct["ending_balance"])

    def __str__(self):
        return f"History Entry for {self.user_id}."

class History():
    fieldnames = ['id', 'user_id', 'account_type', 'transaction_type', 'amount', 'starting_balance', 'ending_balance', 'date']
    filename = "./history.csv"
    id = 0
    history_entries = []
    curr_user_entries = []

    def __init__(self):
        pass

    @classmethod
    def add_transaction_entry(cls, entry_type, acct):
        new_entry = HistoryEntry(entry_type, acct)
        try:
            with open(History.history_file, "a+") as csvfile:
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
                    history_entry = HistoryEntry(row)
                    if history_entry.id >= History.id:
                        History.id = history_entry.id
                    History.history_entries.append(history_entry)
        except csv.Error as e:
            print(e)

    @classmethod
    def get_user_history(cls, user):
        user_history_entries = []
        for entry in History.history_entries:
            if entry.user_id == user.id:
                user_history_entries.append(entry)
        if len(user_history_entries) > 0:
            print("These are your most recent transactions:\n")
            for item in user_history_entries:
                print(f""" 
                    ID:               {item.id}
                    Date:             {item.date}
                    Transaction:      {item.transaction_type}
                    Account Type:     {item.account_type}
                """)
            options = { "1": "See details about an entry", "2": "Return to the main menu."}
            user_choice = None
            while user_choice not in options:
                user_choice = input(f"Would you like to:\n{show_dict_items(options)}")
        else:
            print("You do not have any transactions yet.")
        

    @classmethod
    def display_transaction_detail_for_user(cls, user, transaction_id):
        for acct in History.history_entries:
            if acct.user_id == user.id and acct.id == transaction_id:
                print(f""" 
                    Date:             {acct.date}
                    Transaction:      {acct.transaction_type}
                    Account Type:     {acct.account_type}
                    Amount:           {acct.amount}
                    Starting Balance: {acct.starting_balance}
                    Ending Balance    {acct.ending_balance}
                """)