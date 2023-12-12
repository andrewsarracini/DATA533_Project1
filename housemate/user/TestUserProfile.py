# TestUserProfile.py

import unittest
from unittest.mock import patch
import os
import io
from io import StringIO
import pandas as pd
from userprofile import load_user_profiles, create_profile_from_input, append_to_dataframe, save_dataframe_to_csv
from security import string_hash

class TestUserProfile(unittest.TestCase):
    def setUp(self):
        # Create a temporary CSV file for testing
        self.test_csv_filename = 'user_profiles.csv'
        self.test_file_path = os.path.join(os.getcwd(), self.test_csv_filename)
        self.sample_data = {
            'name': ['User 1'],
            'age': [25],
            'email': ['user1@example.com'],
            'username': ['username1'],
            'password': ['password1']
        }
        self.df = pd.DataFrame(self.sample_data)
        self.df.to_csv(self.test_file_path, index=False)

    def tearDown(self):
        # Remove the temporary CSV file after each test
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)
            
    def test_load_user_profiles(self):
        # Test for existing file path
        existing_file_path = 'user_profiles.csv'
        existing_data = {
            'name': ['User 1', 'User 2', 'User 3'],
            'age': [25, 30, 28],
            'email': ['user1@email.com', 'user2@email.com', 'user3@email.com'],
            'username': ['username1', 'username2', 'username3'],
            'password': ['password1', 'password2', 'username3']
        }
        df_existing = pd.DataFrame(existing_data)
        df_existing.to_csv(existing_file_path, index=False)

        # Test for existing file path
        loaded_existing_df = load_user_profiles(existing_file_path)
        self.assertIsNotNone(loaded_existing_df)
        self.assertTrue(isinstance(loaded_existing_df, pd.DataFrame))
        self.assertEqual(len(loaded_existing_df), len(df_existing))

        # Test for non-existent file path
        non_existing_file_path = 'path/to/non_existing_file.csv'
        loaded_non_existing_df = load_user_profiles(non_existing_file_path)
        self.assertIsNone(loaded_non_existing_df)

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

# # Almost got it... but trouble with the while loop
#     def test_create_profile_invalid_age_input(self):
#         inputs = ["invalid", "25", "user@example.com", "valid_username", "valid_password"]  # Inputs for age, email, username, and password

#         with patch('builtins.input', side_effect=inputs):
#             with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
#                 create_profile_from_input()
        
#         # Split output into lines and check if the expected outputs are present
#         output = mock_stdout.getvalue().strip()
#         expected_output = "Invalid input. Please enter a valid integer for age."
#         self.assertIn(expected_output, output)
        
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
            'email': ['user1@email.com'],
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
            'email': 'user2@email.com',
            'username': 'username2',
            'password': 'password2'
        }
        new_df = append_to_dataframe(self.initial_df, new_profile_data)

        # Verify if the new dataframe contains the added profile
        self.assertEqual(len(new_df), len(self.initial_df) + 1)

class TestAppendToDataFrame(unittest.TestCase):
    def setUp(self):
        # Set up initial data for testing append_to_dataframe function
        self.initial_data = {
            'name': ['User 1'],
            'age': [25],
            'email': ['user1@email.com'],
            'username': ['username1'],
            'password': ['password1']
        }
        self.initial_df = pd.DataFrame(self.initial_data)

    def tearDown(self):
        # Clean up after each test
        pass

    def test_append_to_dataframe(self):
        # Test appending when the initial DataFrame is None
        new_profile_data = {
            'name': 'User 2',
            'age': 30,
            'email': 'user2@email.com',
            'username': 'username2',
            'password': 'password2'
        }
        new_df = append_to_dataframe(None, new_profile_data)

        # Verify if the new dataframe contains only the added profile
        self.assertEqual(len(new_df), 1)
        self.assertEqual(new_df['name'].iloc[0], new_profile_data['name'])
        self.assertEqual(new_df['age'].iloc[0], new_profile_data['age'])
        self.assertEqual(new_df['email'].iloc[0], new_profile_data['email'])
        self.assertEqual(new_df['username'].iloc[0], new_profile_data['username'])
        self.assertEqual(new_df['password'].iloc[0], new_profile_data['password'])

        # Test appending when the initial DataFrame is not None
        new_profile_data_2 = {
            'name': 'User 3',
            'age': 28,
            'email': 'user3@email.com',
            'username': 'username3',
            'password': 'password3'
        }
        new_df_2 = append_to_dataframe(self.initial_df, new_profile_data_2)

        # Verify if the new dataframe contains the added profile along with the initial data
        self.assertEqual(len(new_df_2), len(self.initial_df) + 1)
        # You can add more assertions to check the correctness of the appended data


# if __name__ == '__main__':
#     # Create a test suite
#     test_suite = unittest.TestSuite()
#     test_suite.addTest(unittest.makeSuite(TestUserProfile))
#     test_suite.addTest(unittest.makeSuite(TestAppendToDataFrame))
#     test_suite.addTest(unittest.makeSuite(TestSaveDataFrameToCSV))
#     # Create a test runner
#     test_runner = unittest.TextTestRunner()

#     # Run the tests
#     test_runner.run(test_suite)

if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)


