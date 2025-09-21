import csv
import os

# 1.1 Seed Data to CSV
doctor_who_info = [
    { 'Name': 'The First Doctor',  'Actor': 'William Hartnell',  'Number of Episodes': 134 },
    { 'Name': 'The Second Doctor', 'Actor': 'Patrick Troughton', 'Number of Episodes': 119 }, 
    { 'Name': 'The Third Doctor',  'Actor': 'Jon Pertwee',       'Number of Episodes': 128 }, 
    { 'Name': 'The Fourth Doctor', 'Actor': 'Tom Baker',         'Number of Episodes': 172 }, 
    { 'Name': 'The Fifth Doctor',  'Actor': 'Peter Davison',     'Number of Episodes': 69  }
]

fieldnames = ["Name", "Actor", "Number of Episodes"]

# 3.0 Check CSV File Exists (otherwise error thrown!)
# 3.1 Set Headers in the CSVFile 
# 3.2 SEED DATA TO CSV
# 3.3 EXAMPLE: writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
# 3.4 "w" option will allow writing, but NOT appending...
if not os.path.exists("./doctor_who.csv"):
    with open("./doctor_who.csv", 'w', newline='') as csvfile:
        try:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in doctor_who_info:
                writer.writerow(row)
        except csv.Error as e:
            print(e)

def create_account():
    print("THIS IS THE CREATE ACCOUNT FUNCTION@!!")

def access_account():
    print("THIS IS THE ACCESS ACCOUNT FUNCTION@!!")
    try:
        with open("doctor_who.csv", "r") as file:
            contents = csv.DictReader(file)
            for row in contents:
                print(type(contents))
                print(row) #will print: {'Name': 'The First Doctor', 'Actor': 'William Hartnell', 'Number of Episodes': '134'}
                for prop in fieldnames:
                    print(row[prop]) # will print the value of each individual property
    except csv.Error as e:
        print(e)

def init():
    has_account = None

    account_options = ["Y", "N", "Q"]
    while has_account not in account_options:
        has_account = input("Do you have an account?")

    if has_account == "Y":
        access_account()
        
    if has_account == "N":
        print("Create an account?")
        create_account()

init()


