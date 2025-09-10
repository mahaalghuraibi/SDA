import unittest
from PY_code_challenges import c07_format_contacts

if __name__ == "__main__":
    unittest.main()


class TestFormatContacts(unittest.TestCase):
    # -----------------------------------------------------------------
    # Test 1: Multiple contacts
    # Standard use case with three entries. Each should format correctly
    # and be separated by a space and period.
    # -----------------------------------------------------------------
    def test_multiple_contacts(self):
        contacts = {
            "Brian": "333-333-3333",
            "Lenny": "444-444-4444",
            "Daniel": "777-777-7777"
        }
        result = c07_format_contacts.format_contacts(contacts)
        expected = (
            "Brian has a phone number of 333-333-3333. "
            "Lenny has a phone number of 444-444-4444. "
            "Daniel has a phone number of 777-777-7777."
        )
        self.assertEqual(result, expected)

    # -----------------------------------------------------------------
    # Test 2: Single contact
    # Should return a single properly formatted sentence.
    # -----------------------------------------------------------------
    def test_single_contact(self):
        contacts = {"Alice": "123-456-7890"}
        result = c07_format_contacts.format_contacts(contacts)
        expected = "Alice has a phone number of 123-456-7890."
        self.assertEqual(result, expected)

    # -----------------------------------------------------------------
    # Test 3: Empty dictionary
    # Should return an empty string if no contacts are provided.
    # -----------------------------------------------------------------
    def test_empty_contacts(self):
        contacts = {}
        result = c07_format_contacts.format_contacts(contacts)
        expected = ""
        self.assertEqual(result, expected)

    # -----------------------------------------------------------------
    # Test 4: Names with multiple words
    # Handles full names correctly, not just single words.
    # -----------------------------------------------------------------
    def test_full_name_contact(self):
        contacts = {"John Smith": "555-555-5555", "Mary Jane": "666-666-6666"}
        result = c07_format_contacts.format_contacts(contacts)
        expected = (
            "John Smith has a phone number of 555-555-5555. "
            "Mary Jane has a phone number of 666-666-6666."
        )
        self.assertEqual(result, expected)

    # -----------------------------------------------------------------
    # Test 5: Numbers in different formats
    # Should handle phone numbers in any string format consistently.
    # -----------------------------------------------------------------
    def test_various_number_formats(self):
        contacts = {
            "Tom": "(123) 456-7890",
            "Jerry": "987.654.3210"
        }
        result = c07_format_contacts.format_contacts(contacts)
        expected = (
            "Tom has a phone number of (123) 456-7890. "
            "Jerry has a phone number of 987.654.3210."
        )
        self.assertEqual(result, expected)
