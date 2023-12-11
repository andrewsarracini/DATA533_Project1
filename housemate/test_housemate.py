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
    rental_main,
    purchase_main,
    purchase_user_input,
    rental_recommendation_main
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


class TestHousemate(unittest.TestCase):

    @ classmethod
    def classSetUp(clas):
        print('set up class')

    def setUp(self):
        random.seed(123)

    @patch('builtins.input', return_value='1')
    def test_main_menu_choice1(self, mock_input):

        # Redirect stdout to capture print statements
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        main_menu()

        sys.stdout = sys.__stdout__

        # Define expected output
        main_menu_choice = (
            "Welcome to HouseMate! Please choose an option: \n"
            "1. Create Profile\n"
            "2. Login\n"
            "3. Exit HouseMate\n"
        )

        self.assertEqual(capturedOutput.getvalue(), main_menu_choice)

    @patch('builtins.input', return_value='1')
    def test_profile_menu_choice1(self, mock_input):

        # Redirect stdout to capture print statements
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        profile_menu()

        # Reset stdout

        profile_menu_choice = (
            "You are logged in. Please choose an option: \n"
            "1. View Profile Information\n"
            "2. Edit Profile\n"
            "3. Delete Profile\n"
            "4. View available homes\n"
            "5. Logout and return to the main menu\n"
        )

        self.assertEqual(capturedOutput.getvalue(), profile_menu_choice)

    @patch('builtins.input', return_value='1')
    def test_housemate_menu_chioce1(self, mock_input):

        # Redirect stdout to capture print statements
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        housemate_menu()

        # Reset stdout

        housemate_menu_choice = (
            "Find a home today! Please choose an option: \n"
            "1. View ONLY recommendated properties to rent\n"
            "2. View ONLY recommendated properties to purchase\n"
            "3. View available rental properties\n"
            "4. View available purchase properties\n"
            "5. Return to the profile menu\n"
            "6. Logout and return to the main menu\n"
        )

        self.assertEqual(capturedOutput.getvalue(), housemate_menu_choice)

    @patch('builtins.input', return_value='tEsT')
    def test_rental_user_input(self, mock_input):
        self.assertEqual(rental_user_input(), 'test')

    @patch('builtins.input', return_value='ABCD')
    def test_purchase_user_input(self, mock_input):
        self.assertEqual(rental_user_input(), 'abcd')

    # @patch('builtins.input', return_value='None')
    # def test_rental_main(self):
    #     result = rental_main()
    #     self.assertIsNone(result)

    def tearDown(self):
        sys.stdout = sys.__stdout__

    @classmethod
    def tearDownClass(cls):
        # tearDownClass is a requirement
        pass


unittest.main(argv=[''], verbosity=2, exit=False)
