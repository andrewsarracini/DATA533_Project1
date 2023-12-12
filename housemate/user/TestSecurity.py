# TestSecurity.py

import unittest
import pandas as pd
from .security import string_hash, reverseHash, check_credentials

class TestStringHash(unittest.TestCase):
    def setUp(self):
        self.mapped_strings = {}

    def tearDown(self):
        self.mapped_strings = None

    def test_string_hash_basic(self):
        # Test for basic string hashing
        result = string_hash("This is a test to see what happens")
        self.assertEqual(result, 53286)

    def test_string_hash_sensitive_info(self):
        # Test for hashing sensitive information
        result = string_hash("SensitiveInformationIsHere")
        self.assertEqual(result, 33376)

    def test_string_hash_special_characters(self):
        # Test for hashing strings with numbers and symbols
        result = string_hash("What if there are numbers (333!) and symbols too?")
        self.assertEqual(result, 101197)

class TestReverseHash(unittest.TestCase):
    def setUp(self):
        self.mapped_strings = {}

    def tearDown(self):
        self.mapped_strings = None

    def test_reverse_hash_basic(self):
        # Test for reversing hashed values
        string_hashed = "This is a test to see what happens"
        hash_value = string_hash(string_hashed)
        self.mapped_strings[hash_value] = string_hashed

        result = reverseHash(hash_value, self.mapped_strings)
        self.assertEqual(result, string_hashed)

        # Test for a non-existent hash value
        result = reverseHash(12345, self.mapped_strings)
        self.assertIsNone(result)

    def test_reverse_hash_sensitive_info(self):
        # Additional test cases for string_hash2
        string_hash2 = "SensitiveInformationIsHere"
        hash_value_2 = string_hash(string_hash2)

        self.mapped_strings[hash_value_2] = string_hash2

        result_2 = reverseHash(hash_value_2, self.mapped_strings)

        self.assertEqual(result_2, string_hash2)

    def test_reverse_hash_special_characters(self):
        # Additional test cases for string_hash3
        string_hash3 = "What if there are numbers (333!) and symbols too?"
        hash_value_3 = string_hash(string_hash3)

        self.mapped_strings[hash_value_3] = string_hash3

        result_3 = reverseHash(hash_value_3, self.mapped_strings)

        self.assertEqual(result_3, string_hash3)

# class TestCheckCredentials(unittest.TestCase):
#     def setUp(self):
#         self.df = pd.DataFrame({
#             'username': [str(string_hash('username1'))],
#             'password': [str(string_hash('password1'))]
#         })

#     def tearDown(self):
#         self.df = None

#     def test_check_credentials_match(self):
#         # Test for matching credentials in DataFrame
#         result = check_credentials('username1', 'password1', self.df)
#         self.assertTrue(result)

#     def test_check_credentials_no_match(self):
#         # Test for no matching credentials in DataFrame
#         result = check_credentials('Unknown', 'Password', self.df)
#         self.assertFalse(result)

#     def test_check_credentials_none_df(self):
#         # Test when df is None
#         result = check_credentials('username', 'password', None)
#         self.assertFalse(result)
        
class TestCheckCredentials(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({
            'username': [str(string_hash('username1'))],
            'password': [str(string_hash('password1'))]
        })
        self.df2 = pd.DataFrame({
            'username': [str(string_hash('222222222'))],
            'password': [str(string_hash('222222222'))]
        })
        self.df3 = pd.DataFrame({
            'username': [str(string_hash('username3!'))],
            'password': [str(string_hash('password3!'))]
        })
        self.df4 = pd.DataFrame({
            'username': [str(string_hash('USERNAME4'))],
            'password': [str(string_hash('PASSWORD4'))]
        })
        self.result_true1 = check_credentials('username1', 'password1', self.df)
        self.result_true2 = check_credentials('222222222', '222222222', self.df2)
        self.result_true3 = check_credentials('username3!', 'password3!', self.df3)
        self.result_true4 = check_credentials('USERNAME4', 'PASSWORD4', self.df4)
        self.result_false1 = check_credentials('Unknown1', 'Password1', self.df)
        self.result_false2 = check_credentials('333333333', '333333333', self.df2)
        self.result_false3 = check_credentials('Unknown3!', 'Password3!', self.df3)
        self.result_false4 = check_credentials('UNKNOWN', 'UNKNOWN', self.df4)
        self.result_none1 = check_credentials('username1', 'password1', None)
        self.result_none2 = check_credentials('222222222', '222222222', None)
        self.result_none3 = check_credentials('username3!', 'password3!', None)
        self.result_none4 = check_credentials('USERNAME4', 'PASSWORD4', None)

    def tearDown(self):
        self.df = None

    def test_check_credentials_match(self):
        # Test for matching credentials in DataFrame
        self.assertTrue(self.result_true1)
        self.assertTrue(self.result_true2)
        self.assertTrue(self.result_true3)
        self.assertTrue(self.result_true4)

    def test_check_credentials_no_match(self):
        # Test for no matching credentials in DataFrame
        self.assertFalse(self.result_false1)
        self.assertFalse(self.result_false2)
        self.assertFalse(self.result_false3)
        self.assertFalse(self.result_false4)

    def test_check_credentials_none_df(self):
        # Test when df is None
        self.assertFalse(self.result_none1)
        self.assertFalse(self.result_none2)
        self.assertFalse(self.result_none3)
        self.assertFalse(self.result_none4)

# if __name__ == '__main__':
#     # Create a test suite
#     test_suite = unittest.TestSuite()
#     test_suite.addTest(unittest.makeSuite(TestStringHash))
#     test_suite.addTest(unittest.makeSuite(TestReverseHash))
#     test_suite.addTest(unittest.makeSuite(TestCheckCredentials))

#     # Create a test runner
#     test_runner = unittest.TextTestRunner()

#     # Run the tests
#     test_runner.run(test_suite)

unittest.main(argv=[''], verbosity=2, exit=False)


