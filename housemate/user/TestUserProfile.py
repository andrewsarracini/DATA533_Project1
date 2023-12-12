# TestUserProfile.py

import unittest
from unittest.mock import patch
import os
import io
from io import StringIO
import pandas as pd
from .userprofile import load_user_profiles, create_profile_from_input, append_to_dataframe, save_dataframe_to_csv
from .security import string_hash

class TestUserProfile(unittest.TestCase):
    def setUp(self):
        # Create a temporary CSV file for testing
        self.test_csv_filename = 'test_user_profiles.csv'
        self.test_file_path = os.path.join(os.getcwd(), self.test_csv_filename)
        self.sample_data = {
            'name': ['Test User'],
            'age': [25],
            'email': ['test_user@example.com'],
            'username': ['hashed_test_user'],
            'password': ['hashed_password']
        }
        self.df = pd.DataFrame(self.sample_data)
        self.df.to_csv(self.test_file_path, index=False)

    def tearDown(self):
        # Remove the temporary CSV file after each test
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)

    def test_create_profile_from_input(self):
        # Simulate creating a user profile from user input
        profile_data = {
            'name': 'User 1',
            'age': 25,
            'email': 'user1@example.com',
            'username': 'username1',  # Keeping the original username and password
            'password': 'password1'
        }

        # Mock the user input process
        def mock_input(prompt):
            if 'Enter your name: ' in prompt:
                return profile_data['name']
            elif 'Enter your age: ' in prompt:
                return str(profile_data['age'])
            elif 'Enter your email: ' in prompt:
                return profile_data['email']
            elif 'Enter your username (8 characters or more): ' in prompt:
                return profile_data['username']
            elif 'Enter your password (8 characters or more): ' in prompt:
                return profile_data['password']

        with unittest.mock.patch('builtins.input', side_effect=mock_input):
            created_profile_data = create_profile_from_input()

        # Hash the username and password before assertion
        hashed_username = string_hash(profile_data['username'])
        hashed_password = string_hash(profile_data['password'])

        # Replace the original username and password with hashed values
        profile_data['username'] = hashed_username
        profile_data['password'] = hashed_password

        # Verify if the created profile matches the expected data
        self.assertEqual(created_profile_data, profile_data)
        
    # def test_age_input_edge_cases(self):
    #     # Edge cases for age input
    #     age_test_cases = [
    #         (10, "Invalid input. Please enter an integer for age."),
    #         (1000, "Invalid age. Please enter an integer between 11 and 999."),
    #         (20, None)  # A valid age
    #         # Add more test cases for other conditions if needed
    #     ]

    #     for age, expected_output in age_test_cases:
    #         with self.subTest(age=age), patch('builtins.input', side_effect=[str(age)]):
    #             captured_output = StringIO()
    #             with patch('sys.stdout', captured_output):
    #                 create_profile_from_input()
    #             output = captured_output.getvalue().strip()
                
    #             if expected_output:
    #                 self.assertIn(expected_output, output)
    #             else:
    #                 # Valid age, loop should exit
    #                 self.assertNotIn("Invalid", output)

class TestAppendToDataFrame(unittest.TestCase):
    def setUp(self):
        # Set up initial data for testing append_to_dataframe function
        self.initial_data = {
            'name': ['User 1'],
            'age': [25],
            'email': ['user1@example.com'],
            'username': ['username1'],
            'password': ['password1']
        }
        self.initial_df = pd.DataFrame(self.initial_data)

    def tearDown(self):
        # Clean up after each test
        pass

    def test_append_to_dataframe(self):
        # Append a new profile to the existing dataframe
        new_profile_data = {
            'name': 'User 2',
            'age': 30,
            'email': 'user2@example.com',
            'username': 'username2',
            'password': 'password2'
        }
        new_df = append_to_dataframe(self.initial_df, new_profile_data)

        # Verify if the new dataframe contains the added profile
        self.assertEqual(len(new_df), len(self.initial_df) + 1)

class TestSaveDataFrameToCSV(unittest.TestCase):
    def setUp(self):
        # Set up initial data for testing save_dataframe_to_csv function
        self.test_data = {
            'name': ['User 1'],
            'age': [30],
            'email': ['user1@example.com'],
            'username': ['username1'],
            'password': ['password1']
        }
        self.test_df = pd.DataFrame(self.test_data)
        self.test_file_path = os.path.join(os.getcwd(), 'test_save.csv')

    def tearDown(self):
        # Clean up after each test
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)

    def test_save_dataframe_to_csv(self):
        # Save the dataframe to a temporary CSV file
        save_dataframe_to_csv(self.test_df, self.test_file_path)

        # Check if the file was created and contains data
        self.assertTrue(os.path.exists(self.test_file_path))
        loaded_df = load_user_profiles(self.test_file_path)
        self.assertIsNotNone(loaded_df)
        self.assertEqual(len(loaded_df), len(self.test_df))

# if __name__ == '__main__':
#     # Create a test suite
#     test_suite = unittest.TestSuite()
#     result = unittest.TestResult()
#     test_suite.addTest(unittest.makeSuite(TestUserProfile))
#     test_suite.addTest(unittest.makeSuite(TestAppendToDataFrame))
#     test_suite.addTest(unittest.makeSuite(TestSaveDataFrameToCSV))

#     # Create a test runner
#     test_runner = unittest.TextTestRunner()

#     # Run the tests WRAPPED PRINT
#     print(test_runner.run(test_suite))
    
# my_suite()

unittest.main(argv=[''], verbosity=2, exit=False)


