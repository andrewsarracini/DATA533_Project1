import profile
import unittest
from unittest.mock import patch, MagicMock

import sys
import io
import os
import pandas as pd
import random


from housemate import (
    main_menu,
    profile_menu,
    housemate_menu,
    rental_user_input,
    purchase_user_input,
    rental_main,
    purchase_main,
    rental_recommendation_main,
    get_file_path
)

from user.security import string_hash, reverseHash, check_credentials
from user.userprofile import (
    UserProfile,
    load_user_profiles,
    create_profile_from_input,
    append_to_dataframe,
    save_dataframe_to_csv
)
from user.userlogin import view_profile, edit_profile, delete_profile

from property.property import Property
from property.purchase import (
    Purchase,
    Condo,
    TownHome,
    Duplex,
    Bungalow,
    TwoStory,
    Mansion,
    gen_purchase,
    view_purchase_list,
    purchase_recommendation
)

from property.rental import (
    Rental,
    RentalCondo,
    RentalTownHome,
    RentalDuplex,
    RentalBungalow,
    RentalTwoStory,
    RentalMansion,
    gen_rental,
    view_rental_list,
    rental_recommendation
)


class TestMenus(unittest.TestCase):

    @ classmethod
    def classSetUp(clas):
        pass

    def setUp(self):
        random.seed(123)
        self.main_output = (
            "Welcome to HouseMate! Please choose an option: \n"
            "1. Create Profile\n"
            "2. Login\n"
            "3. Exit HouseMate\n")
        self.profile_output = (
            "You are logged in. Please choose an option: \n"
            "1. View Profile Information\n"
            "2. Edit Profile\n"
            "3. Delete Profile\n"
            "4. View available homes\n"
            "5. Logout and return to the main menu\n"
        )
        self.housemate_output = (
            "Find a home today! Please choose an option: \n"
            "1. View ONLY recommendated properties to rent\n"
            "2. View ONLY recommendated properties to purchase\n"
            "3. View available rental properties\n"
            "4. View available purchase properties\n"
            "5. Return to the profile menu\n"
            "6. Logout and return to the main menu\n")

    def test_main_menu_choices(self):
        choices = {
            '1': self.main_output,
            '2': self.main_output,
            '3': self.main_output
        }

        for choice, main_output in choices.items():
            with self.subTest(choice=choice):
                with patch('builtins.input', return_value=choice), \
                        io.StringIO() as capturedOutput:
                    sys.stdout = capturedOutput

                    main_menu()

                    sys.stdout = sys.__stdout__

                    self.assertEqual(capturedOutput.getvalue(), main_output)

    def test_profile_menu_choices(self):
        profile_choices = {
            '1': self.profile_output,
            '2': self.profile_output,
            '3': self.profile_output,
            '4': self.profile_output,
            '5': self.profile_output
        }

        for profile_choice, profile_output in profile_choices.items():
            with self.subTest(profile_choice=profile_choice):
                with patch('builtins.input', return_value=profile_choice), \
                        io.StringIO() as capturedOutput:
                    sys.stdout = capturedOutput

                    profile_menu()

                    sys.stdout = sys.__stdout__

                    self.assertEqual(capturedOutput.getvalue(), profile_output)

    def test_profile_menu_choices(self):
        housemate_choices = {
            '1': self.housemate_output,
            '2': self.housemate_output,
            '3': self.housemate_output,
            '4': self.housemate_output,
            '5': self.housemate_output,
            '6': self.housemate_output
        }

        for housemate_choice, housemate_output in housemate_choices.items():
            with self.subTest(housemate_choice=housemate_choice):
                with patch('builtins.input', return_value=housemate_output), \
                        io.StringIO() as capturedOutput:
                    sys.stdout = capturedOutput

                    housemate_menu()

                    sys.stdout = sys.__stdout__

                    self.assertEqual(
                        capturedOutput.getvalue(), housemate_output)

    def tearDown(self):
        sys.stdout = sys.__stdout__

    @classmethod
    def tearDownClass(cls):
        # tearDownClass is a requirement
        pass


unittest.main(argv=[''], verbosity=2, exit=False)


class TestHelperFunctions(unittest.TestCase):
    @ classmethod
    def classSetUp(clas):
        pass

    def setUp(self):
        random.seed(123)

    def test_get_file_path(self):
        self.assertEqual(get_file_path(), os.getcwd()+"\\user_profiles.csv")

    @patch('builtins.input', return_value='tEsT')
    def test_rental_user_input(self, mock_input):
        self.assertEqual(rental_user_input(), 'test')

    @patch('builtins.input', return_value='ABCD')
    def test_purchase_user_input(self, mock_input):
        self.assertEqual(purchase_user_input(), 'abcd')

    def tearDown(self):
        sys.stdout = sys.__stdout__

    @classmethod
    def tearDownClass(cls):
        # tearDownClass is a requirement
        pass
