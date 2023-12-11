# TestUserLogin.py

import unittest
from unittest.mock import patch
import pandas as pd
import os
from io import StringIO
from userlogin import login_get_file_path, view_profile, edit_profile, delete_profile
from userprofile import load_user_profiles
from security import string_hash

class TestUserProfileLoading(unittest.TestCase):
    def setUp(self):
        # Create a temporary CSV file for testing with the expected filename
        self.test_csv_filename = 'user_profiles.csv'
        with open(self.test_csv_filename, 'w') as file:
            file.write('user1,25,user1@email.com,username1,password1\n')
            file.write('user2,30,user2@email.com,username2,password2\n')
            file.write('user3,28,user3@email.com,username3,password3\n')

    def test_login_get_file_path(self):
        # Test the login_get_file_path function
        expected_path = os.path.abspath(self.test_csv_filename)
        file_path = login_get_file_path()
        self.assertEqual(file_path, expected_path)

    def test_load_user_profiles(self):
        # Test the load_user_profiles function
        file_path = os.path.abspath(self.test_csv_filename)
        user_profiles = load_user_profiles(file_path)

        # Ensure user_profiles is a DataFrame and has data rows
        self.assertIsInstance(user_profiles, pd.DataFrame)
        self.assertGreater(len(user_profiles), 0)
        
    def tearDown(self):
        # Remove the temporary CSV file after the test
        os.remove(self.test_csv_filename)
        
class TestViewProfile(unittest.TestCase):
    def setUp(self):
        # Create a temporary CSV file for testing with the expected filename
        self.test_csv_filename = 'user_profiles.csv'
        self.sample_data = {
            'name': ['User 1', 'User 2', 'User 3'],
            'age': [25, 30, 28],
            'email': ['user1@email.com', 'user2@email.com', 'user3@email.com'],
            'username': ['username1', 'username2', 'username3'],
            'password': ['password1', 'password2', 'password3']
        }
        self.df = pd.DataFrame(self.sample_data)

        # Write DataFrame to CSV for testing
        self.df.to_csv(self.test_csv_filename, index=False)

    def test_view_profile_existing_user(self):
        # Define user data to simulate user's profile information
        user_profile_data = {
            'name': ['User 1'],
            'age': [25],
            'email': ['user1@email.com'],
            'username': ['3337'],  # Hashed value for username to match
            'password': ['3479']   # Hashed value for password to match
        }

        # Create a DataFrame with the user profile data
        user_df = pd.DataFrame(user_profile_data)

        # Simulate the function call and capture the output
        with unittest.mock.patch('sys.stdout', new=StringIO()) as fake_output:
            # Username can be a string here because it will be hashed within view_profile
            view_profile('username1', user_df)  # Pass the original username for testing
            captured_output = fake_output.getvalue().strip()

        expected_output = (
            "Profile Information:\n     name  age            email username password\n"
            "0  User 1   25  user1@email.com     3337     3479"
        ).strip()  # Strip trailing whitespaces or line breaks

        # Compare the captured output with the expected output
        self.assertEqual(expected_output, captured_output)

    def test_view_profile_nonexistent_user(self):
        # Test for a non-existing user profile
        expected_output = "No profile information found for this user.\n"
        with unittest.mock.patch('sys.stdout', new=StringIO()) as fake_output:
            view_profile('nonexistent_user', self.df)
            self.assertEqual(fake_output.getvalue(), expected_output)
            
    def tearDown(self):
        # Remove the temporary CSV file after each test
        if os.path.exists(self.test_csv_filename):
            os.remove(self.test_csv_filename)

class TestEditProfile(unittest.TestCase):
    def setUp(self):
        self.sample_data = {
            'name': ['John'],
            'age': [30],
            'email': ['john@email.com'],
            'username': ['username1'],
            'password': ['password1']
            # Add more columns as needed
        }
        self.df = pd.DataFrame(self.sample_data)

    @patch('builtins.input', side_effect=['email', 'new_email@email.com'])
    def test_edit_profile_existing_field(self, mock_input):
        expected_output = "Profile updated successfully!\n"
        result = edit_profile('user1', self.df)
        self.assertEqual(result, ("no_change", None))

    @patch('builtins.input', side_effect=['invalid_field'])
    def test_edit_profile_invalid_field(self, mock_input):
        expected_output = "Invalid field name. Profile not updated.\n"
        result = edit_profile('user1', self.df)
        self.assertEqual(result, ("no_change", None))
        
    def tearDown(self):
        # Reset or clear any changes made during the tests
        self.sample_data = None
        self.df = None
        
class TestDeleteProfile(unittest.TestCase):
    def setUp(self):
        # Create a temporary CSV file for testing with the expected filename
        self.test_csv_filename = 'user_profiles.csv'
        self.sample_data = {
            'name': ['User 1', 'User 2', 'User 3'],
            'age': [25, 30, 28],
            'email': ['user1@email.com', 'user2@email.com', 'user3@email.com'],
            'username': ['username1', 'username2', 'username3'],
            'password': ['password1', 'password2', 'password3']
        }
        self.df = pd.DataFrame(self.sample_data)

        # Write DataFrame to CSV for testing
        self.df.to_csv(self.test_csv_filename, index=False)

    @patch('builtins.input', return_value='yes')
    def test_delete_profile_confirmation_yes(self, mock_input):
        expected_output = "Profile deleted successfully!\n"
        result = delete_profile('username1', self.df)
        self.assertEqual(result, '3337')

    @patch('builtins.input', return_value='no')
    def test_delete_profile_confirmation_no(self, mock_input):
        expected_output = "Profile deletion canceled.\n"
        result = delete_profile('username1', self.df)
        self.assertEqual(result, '3337')

    def tearDown(self):
        # Remove the temporary CSV file after each test
        if os.path.exists(self.test_csv_filename):
            os.remove(self.test_csv_filename)

# if __name__ == '__main__':
#     # Create a test suite
#     test_suite = unittest.TestLoader().loadTestsFromTestCase(TestUserProfileLoading)
#     # Create a test runner
#     test_runner = unittest.TextTestRunner()

#     # Run the tests
#     test_runner.run(test_suite)

if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)


