############################# CUSTOMER CLASS #############################################
class Customer:

    def __init__(self, row):
        self.id         = int(row["id"])
        self.first_name = row["first_name"]
        self.last_name  = row["last_name"]
        self.password   = row["password"]
        self.checking   = False if row["checking"] == "False" else int(row["checking"])
        self.savings    = False if row["savings"]  == "False" else int(row["savings"])
        self.active     = True  if row["active"]   == "True"  else False
        self.overdraft_count = int(row["overdraft_count"])
    
    def __str__(self):
        return f" Account info: {self.id} {self.first_name} {self.last_name} {self.password} {self.checking} {self.savings} {self.active} {self.overdraft_count}"

    @classmethod
    def get_new_user(cls):
        return { 
            "id":              0, 
            "first_name":      "", 
            "last_name":       "", 
            "password":        "", 
            "checking":        "False", 
            "savings":         "False",
            "active":          "True",
            "overdraft_count": 0,
        }