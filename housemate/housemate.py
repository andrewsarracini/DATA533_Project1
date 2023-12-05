# housemate.py module

import os
import pandas as pd
from user.security import stringHash, reverseHash, check_credentials
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

# --------------------------------- functions start here --------------------------------- #

# Function to establish file_path and load user profiles from CSV file using load_user_profiles from userprofile.py module
def get_file_path():
    # Using a relative path (will stored in the user's home directory)
    relative_path = 'user/user_profiles.csv'
    if os.path.exists(relative_path):
        return relative_path

    # If the file is not found, return a default path in the user's home directory
    home_dir = os.path.expanduser('~')
    default_path = os.path.join(home_dir, 'user_profiles.csv')
    return default_path

file_path = get_file_path()
user_profiles = load_user_profiles(file_path)

# Function to display main menu options
def main_menu():
    print("Welcome to HouseMate! Please choose an option: ")
    print("1. Create Profile")
    print("2. Login")
    print("3. Exit HouseMate")

# Function to display profile menu options
def profile_menu():
    print("You are logged in. Please choose an option: ")
    print("1. View Profile Information")
    print("2. Edit Profile")
    print("3. Delete Profile")
    print("4. View available homes")
    print("5. Logout and return to the main menu")
    
# Function to display the housemate menu options
def housemate_menu(): 
    print("Find a home today! Please choose an option: ")
    print("1. View ONLY recommendated properties to rent")
    print("2. View ONLY recommendated properties to purchase*")
    print("3. View available rental properties")
    print("4. View available purchase properties")
    print("5. Return to the profile menu")
    print("6. Logout and return to the main menu")
    
# Function to obtain the user input and assign to a variable for use in casting onto a class
def rental_user_input():
    print("Enter the preferred type of property (Condo/TownHome/Duplex/Bungalow/TwoStory/Mansion): ")
    user_input = input().lower()
    return user_input

# Function to obtain the mapped user input using rental_user_input() above, to a variable to be called into a function from rental.py
def rental_main():
    while True:
        try:
            rent_n = int(input("Enter the number of rental properties you would like to view (1-9): "))
            if 1 <= rent_n <= 9:
                while True:
                    user_pref = rental_user_input()

                    if user_pref == 'condo': # Ensure RentalCondo, RentalTownHome, etc., are the class names, not instances
                        pref_type = RentalCondo
                    elif user_pref == 'townhome':
                        pref_type = RentalTownHome
                    elif user_pref == 'duplex':
                        pref_type = RentalDuplex
                    elif user_pref == 'bungalow':
                        pref_type = RentalBungalow
                    elif user_pref == 'twostory':
                        pref_type = RentalTwoStory
                    elif user_pref == 'mansion':
                        pref_type = RentalMansion
                    else:
                        print("Invalid property type entered. Please try again.")
                        continue

                    rental_list = gen_rental(rent_n, pref_type)
                    view_rental_list(rental_list)
                    break
                break
            else:
                print("The number of properties should be between 1 and 9.")
        except ValueError:
            print("Please enter only whole numbers.")

# Function to obtain the user input and assign to a variable for use in casting onto a class 
def purchase_user_input():
    print("Enter the preferred type of property (Condo/TownHome/Duplex/Bungalow/TwoStory/Mansion): ")
    user_input = input().lower()
    return user_input

# Function to obtain the mapped user input using purchase_user_input() above, to a variable to be called into a function from purchase.py
def purchase_main():
    while True:
        try: 
            purchase_n = int(input("Enter the number of purchase properties you would like to view (1-9): "))
            if 1 <= purchase_n <= 9:
                while True:
                    user_pref = purchase_user_input()
                    
                    if user_pref == 'condo': # Ensure Condo, TownHome, etc., are the class names, not instances
                        pref_type = Condo
                    elif user_pref == 'townhome':
                        pref_type = TownHome
                    elif user_pref == 'duplex':
                        pref_type = Duplex
                    elif user_pref == 'bungalow':
                        pref_type = Bungalow
                    elif user_pref == 'twostory':
                        pref_type = TwoStory
                    elif user_pref == 'mansion':
                        pref_type = Mansion
                    else:
                        print("Invalid property type entered. Please try again.")
                        continue

                    purchase_list = gen_purchase(purchase_n, pref_type)
                    view_purchase_list(purchase_list)
                    break
                break 
            else:
                print("The number of properties should be between 1 and 9.")
        except ValueError:
            print("Please enter only whole numbers.")
            
# Function to obtain the mapped user input using rental_user_input() above, to a variable to be called into a function from rental.py
def rental_recommendation_main():
    while True:
        try: 
            income = int(input("Enter your annual salary: "))
            while not (1 <= income <= 10000000):
                print("Please enter an annual salary between 1 and $10,000,000")
                income = int(input("Enter your annual salary: "))

            pref_beds = int(input("Enter the number of bedrooms you would prefer: "))
            while not (1 <= pref_beds <= 10):
                print("Please enter a preferred number of bedrooms between 1 and 10")
                pref_beds = int(input("Enter the number of bedrooms you would prefer: "))

            prop_type = rental_user_input()
            prop_type_mapping = {
                'condo': RentalCondo, # Ensure RentalCondo, RentalTownHome, etc., are the class names, not instances
                'townhome': RentalTownHome,
                'duplex': RentalDuplex,
                'bungalow': RentalDuplex,
                'twostory': RentalTwoStory,
                'mansion': RentalMansion
            }

            rec_rent_list = []
            if prop_type in prop_type_mapping:
                prop_class = prop_type_mapping[prop_type]  # Retrieve class from the mapping
                rec_rent_list = view_rental_list(rental_recommendation(prop_class, income, pref_beds))
                # Display rental recommendations
                break
            else:
                print("Invalid property type entered. Please try again.")

            break # Exiting the input loop once all inputs are taken

        except ValueError:
            print("Please enter only whole numbers.")

# Function use the map user input using purchase_user_input() above, to an variable to be called into a function from purchase.py         
def purchase_recommendation_main():
    while True:
        try: 
            downpay = int(input("Enter the amount you have for a downpayment: "))
            while not (1 <= downpay <= 10000000):
                print("Please enter a downpayment between 1 and $10,000,000")
                downpay = int(input("Enter the amount you have for a downpayment: "))

            income = int(input("Enter your annual salary: "))
            while not (1 <= income <= 10000000):
                print("Please enter an annual salary between 1 and $10,000,000")
                income = int(input("Enter your annual salary: "))

            pref_beds = int(input("Enter the number of bedrooms you would prefer: "))
            while not (1 <= pref_beds <= 10):
                print("Please enter a preferred number of bedrooms between 1 and 10")
                pref_beds = int(input("Enter the number of bedrooms you would prefer: "))

            prop_type = purchase_user_input()
            prop_type_mapping = {
                'condo': Condo, # Ensure Condo, TownHome, etc., are the class names, not instances
                'townhome': TownHome,
                'duplex': Duplex,
                'bungalow': Bungalow,
                'twostory': TwoStory,
                'mansion': Mansion
            }

            rec_pur_list = []
            if prop_type in prop_type_mapping:
                prop_class = prop_type_mapping[prop_type]  # Retrieve class from the mapping
                rec_pur_list = view_purchase_list(purchase_recommendation(prop_class, downpay, income, pref_beds))
                # Display purchase recommendations
                break

            else:
                print("Invalid property type entered. Please try again.")

            break # Exiting the input loop once all inputs are taken

        except ValueError:
            print("Please enter only whole numbers.")

# --------------------------------- functions end here --------------------------------- #

status = True

while status == True:
    main_menu_active = True # Setting main menu flag to true for flow control
    while main_menu_active == True:
        main_menu()
        choice = input("Enter your choice (1-3): ")
        
        # Load user profiles from CSV file using load_user_profiles from userprofile.py module
        user_profiles = load_user_profiles(file_path)

        if choice == '1':
            # Conditional if statement to ensure that the create profile function isn't implicitly called in userlogin.py module
            if __name__ == "__main__":
                file_name = 'user_profiles.csv'

                existing_df = load_user_profiles(file_path)

                # Conditional if statement that checks if there is an existing dataframe, if not create one
                if existing_df is None:
                    existing_df = pd.DataFrame()

                # While there is a dataframe, take in the user input and concatenate to the existing dataframe
                while True:
                    user_profile_data = create_profile_from_input()
                    existing_df = append_to_dataframe(existing_df, user_profile_data)

                    # Ask if the user wants to add another profile
                    choice = input("Do you want to add another profile? (yes/no): ").lower()
                    if choice != 'yes':
                        break
                
            main_menu_active = True # Setting main menu flag to false for flow control (sent back to main menu to login)
        elif choice == '2':
            # User login to get to the profile menu
            # While loop to take in the username and password and match to credentials stored in CSV, if no match continues asking
            
            # User is allowed 3 attempts before being exited
            max_attempts = 3
            attempts = 0

            while attempts < max_attempts:
                username = input("Enter your username or 's' to stop: ")
                if username == 's':
                    break
                password = input("Enter your password or 's' to stop: ")
                if password == 's':
                    break
                
                if check_credentials(username, password, user_profiles):
                    print("Login Successful!")
                    break
                else:
                    attempts += 1
                    remaining_attempts = max_attempts - attempts
                    if remaining_attempts > 0:
                        print(f"Invalid credentials. {remaining_attempts} attempts remaining.")
                    else:
                        print("Maximum attempts reached. Exiting.")
                        break
            main_menu_active = False # Setting main menu flag to false for flow control (sent to the next menu)
        elif choice == '3':
            print("Exiting HouseMate. Have a great day!")
            status = False
            main_menu_active = False # Setting main menu flag to false for flow control (exits from application)
        else:
            print("Invalid choice. Please enter a number between 1 and 3 or 'q' to exit HouseMate.")

    if status == False:
        break
    
    profile_menu_active = True # Setting the profile menu flag to true for flow control
    while profile_menu_active == True:
        # Profile menu after successful login
        profile_menu()
        choice = input("Enter your choice (1-5) or 'q' to exit HouseMate: ")

        if choice == '1':
            # View Profile Information
            view_profile(username, user_profiles)
        elif choice == '2':
            # Edit Profile
            edit_result, new_value = edit_profile(username, user_profiles)
            if edit_result == "username_changed":
                print("Username has been changed. Please login again.")
                break # Exit the profile menu loop when the username or password is edited (to re login)
            elif edit_result == "password_changed":
                print("Password has been changed. Please login again.")
                break # Exit the profile menu loop when the username or password is edited (to re login)
        elif choice == '3':
            deleted_user = delete_profile(username, user_profiles) # Utilize the decorated function
            if stringHash(username) == deleted_user:
                print("Profile has been deleted. Please log in again.")
            break  # Exit the profile menu loop when the user's profile is deleted (sent to the main menu)
        elif choice == '4':
            housemate_menu_active = True # Setting housemate menu flag to true for flow control
            while housemate_menu_active == True:
                # Housemate menu for selecting recommendations or viewing all
                housemate_menu()
                choice = input("Enter your choice (1-5) or 'q' to exit HouseMate: ")

                if choice == '1':
                    # Rental recommendation list based on user input
                    rental_recommendation_main()
                    continue                
                if choice == '2':
                    # Purchase recommendation list based on user input
                    purchase_recommendation_main()
                    continue        
                elif choice == '3':
                    # Find a home to rent
                    print("This is finding you a home to rent")
                    if __name__ == "__main__":
                        rental_main()
                    continue
                elif choice == '4':
                    # Find a home to purchase
                    print("This is finding you a home to purchase")
                    if __name__ == "__main__":
                        purchase_main()
                    continue
                elif choice == '5':
                    # Return to the main menu
                    print("This is returning to the profile menu")
                    housemate_menu_active = False # Setting housemate menu flag to false for flow control (sent to profile menu)
                elif choice == '6':
                    # Logout and return to the main menu
                    print("This is returning to the main menu.")
                    housemate_menu_active = False # Setting housemate menu flag to false for flow control (sent to profile menu)
                    profile_menu_active = False # Setting profile menu flag to false for flow control (sent to the main menu)
                elif choice.lower() == 'q':
                    # Exit HouseMate when 'q' is entered (exits application)
                    print("Exiting HouseMate. Have a great day!")
                    status = False
                    housemate_menu_active = False # Setting housemate menu flag to false for flow control
                    profile_menu_active = False # Setting profile menu flag to false for flow control
                    main_menu_active = False # Setting main menu flag to false for flow control
                else:
                    print("Invalid choice. Please enter a number between 1 and 5 or 'q' to exit HouseMate.")
        elif choice == '5':
            # Logout and return to the main menu
            print("This is returning to the main menu.")
            break  # Exit the menu loop when logging out
        elif choice.lower() == 'q':
            print("Exiting HouseMate. Have a great day!")
            status = False
            break  # Exit HouseMate when 'q' is entered (exits application)
        else:
            print("Invalid choice. Please enter a number between 1 and 5 or 'q' to exit HouseMate.")
    
    if status == False:
        break # Exit the outer while loop when the user chooses to exit HouseMate
    
    
