import csv

############################# SEED DATA BELOW #############################################
customers = [
    { 'id': 10001, "first_name": 'William', 'last_name': "Hartnell",  "password": "4fg56",     "checking": 100,   "savings": False,   "active": True,  "overdraft_count": 0 },
    { 'id': 10002, "first_name": 'Patrick', 'last_name': "Troughton", "password": "serf",      "checking": False, "savings": 200,     "active": True,  "overdraft_count": 1 }, 
    { 'id': 10003, "first_name": 'Jon ',    'last_name': "Pertwee",   "password": "233!",      "checking": -65,   "savings": 250,     "active": False, "overdraft_count": 2 }, 
    { 'id': 10004, "first_name": 'Tom ',    'last_name': "Baker",     "password": "ee",        "checking": 0,     "savings": False,   "active": True,  "overdraft_count": 0 }, 
    { 'id': 10005, "first_name": 'Peter ',  'last_name': "Davison",   "password": "werf345",   "checking": 58,    "savings": False,   "active": False, "overdraft_count": 4 },
    { 'id': 10006, "first_name": 'Suresh ', 'last_name': "Sigera",    "password": "wergt",     "checking": 63,    "savings": False,   "active": False, "overdraft_count": 3 },
    { 'id': 10007, "first_name": 'James ',  'last_name': "Taylor",    "password": "#@FG",      "checking": -10,   "savings": 0,       "active": False, "overdraft_count": 2 },
    { 'id': 10008, "first_name": 'Melvin ', 'last_name': "Gordon",    "password": "GD4dS",     "checking": -35,   "savings": 2567,    "active": True,  "overdraft_count": 1 },
    { 'id': 10009, "first_name": 'Stacey ', 'last_name': "Abrams",    "password": "!fiuenrg",  "checking": False, "savings": 3452345, "active": True,  "overdraft_count": 1 },
    { 'id': 100010, "first_name": 'Jake ',  'last_name': "Paul",      "password": "wegtr",     "checking": 10000, "savings": -10,     "active": True,  "overdraft_count": 0 },
]

fieldnames = ['id', "first_name", 'last_name', "password", "checking", "savings", "active", "overdraft_count"]

def generate_seed_data():
    with open("./bank.csv", 'w', newline='') as csvfile:
        try:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in customers:
                writer.writerow(row)
        except csv.Error as e:
            print(e)