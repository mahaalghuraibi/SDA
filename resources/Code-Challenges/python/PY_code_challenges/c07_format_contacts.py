# -----------------------------------------------------------------
# Challenge: 07_format_contacts
# Prompt:
# Write a function called `format_contacts` that takes a
# dictionary of key-value pairs that includes the name of the contact as the key
# and their phone numbers as the value. Return a formatted string that says:
# "{Name} has a phone number of {number}" for each entry and includes
# all contacts in the dictionary with a space between each entry and a period at the 
# end of each sentence.
#
# Example response:
# "Brian has a phone number of 333-333-3333. Lenny has a phone number of 444-444-4444. Daniel has a phone number of 777-777-7777."
# 
# Example function call:
# format_contacts({'Brian': '333-333-3333', 'Lenny': '444-444-4444', 'Daniel': '777-777-7777'})
# 
# -----------------------------------------------------------------

def format_contacts(contacts):
    return