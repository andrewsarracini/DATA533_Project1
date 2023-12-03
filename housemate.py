# housemate.py module

import pandas as pd
from security import stringHash, reverseHash, check_credentials
from userprofile import (
    UserProfile,
    load_user_profiles,
    create_profile_from_input,
    append_to_dataframe,
    save_dataframe_to_csv
)
from userlogin import view_profile, edit_profile, delete_profile

from property import Property
from purchase import (
    Purchase, 
    Condo,
    TownHome,
    Duplex,
    Bungalow,
    TwoStory,
    Mansion,
    gen_purchase, 
    view_purchase_list
)
from rental import (
    Rental,
    RentalCondo,
    RentalTownHome,
    RentalDuplex,
    RentalBungalow,
    RentalTwoStory,
    RentalMansion,
    gen_rental,
    view_rental_list,
)

# Load user profiles from CSV file using load_user_profiles from userprofile.py module
file_path = r'C:\Users\\OneDrive\Desktop\DATA533\Project\housemate\user\user_profiles.csv'
user_profiles = load_user_profiles(file_path)

# -------------------------------------------------------------------------------------------------------------------------------------------- functions start here ------------------------------------------

# Function to display main menu options ------------------------------- changed from display_menu to main_menu
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
    
# Function to display the housemate menu options --------------------- added ---------------
def housemate_menu(): 
    print("Find a home today! Please choose an option: ")
    print("1. *Recommendation algorithm here*")
    print("2. View available rental properties")
    print("3. View available purchase properties")
    print("4. Return to the profile menu")
    print("5. Logout and return to the main menu")
    
# Function to obtain the user input and assign to a variable for use in casting onto a class
def rental_user_input():
    print("Enter the preferred type of property (Condo/TownHome/Duplex/Bungalow/TwoStory/Mansion): ")
    user_input = input().lower()
    return user_input

# Function to map user input to an object to be called into a function from rental.py
def rental_main():
    while True:
        try:
            rent_n = int(input("Enter the number of rental properties you would like to view: "))
            if 1 <= rent_n <= 9:
                while True:
                    user_pref = rental_user_input()

                    if user_pref == 'condo':
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

# Function to map user input to an object to be called into a function from purchase.py
def purchase_main():
    while True:
        try: 
            purchase_n = int(input("Enter the number of purchase properties you would like to view (1-9): "))
            if 1 <= purchase_n <= 9:
                while True:
                    user_pref = purchase_user_input()
                    
                    if user_pref == 'condo':
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

# -------------------------------------------------------------------------------------------------------------------------------------------------- functions end here ---------------------------------------

status = True # added to exit from HouseMate during while loops ------------------------------ CHANGED

while status == True:
    main_menu_active = True # ------------------------------------------------------------------------------------------ ADDED 5:55am figured it out
    while main_menu_active == True: # ------------------------------------------------------------------------------------------ ADDED 5:55am figured it out
        main_menu()
        choice = input("Enter your choice (1-3): ")
        
        # Load user profiles from CSV file using load_user_profiles from userprofile.py module
        file_path = r'C:\Users\cadla\OneDrive\Desktop\DATA533\Project\housemate\user\user_profiles.csv'
        user_profiles = load_user_profiles(file_path)

        if choice == '1':
            # Conditional if statement to ensure that the create profile function isn't implicitly called in userlogin.py module
            if __name__ == "__main__":
                file_name = 'user_profiles.csv'
                file_path = r'C:\Users\cadla\OneDrive\Desktop\DATA533\Project\housemate\user\user_profiles.csv'

                existing_df = load_user_profiles(file_path)

                # Conditional if statement that checks if there is an existing dataframe, if not create one
                if existing_df is None:
                    existing_df = pd.DataFrame()

                # While there is a dataframe, take in the user input and append to the existing dataframe
                while True:
                    user_profile_data = create_profile_from_input()
                    existing_df = append_to_dataframe(existing_df, user_profile_data)

                    # Ask if the user wants to add another profile
                    choice = input("Do you want to add another profile? (yes/no): ").lower()
                    if choice != 'yes':
                        break
                # Save DataFrame to CSV
                # Use hashed_username and hashed_password in the CSV
                save_dataframe_to_csv(existing_df, file_path)
                print("User Profile DataFrame:")
                print(existing_df)
            main_menu_active = False # ------------------------------------------------------------------------------------------ ADDED 5:55am figured it out
        elif choice == '2':
            # User login to get to the login menu
            # While loop to take in the username and password and match to credentials stored in CSV, if no match continues asking --------------------- might need to add an escape
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

                # if username == 's' or password == 's':
                #     break
                
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
            main_menu_active = False # ------------------------------------------------------------------------------------------ ADDED 5:55am figured it out

        elif choice == '3':
            print("Exiting HouseMate. Have a great day!")
            status = False
            # break # Exit HouseMate because the user is at the main menu # ------------------------------------------------------------------------- REMOVED 5:55am figured it out
            main_menu_active = False # ------------------------------------------------------------------------------------------ ADDED 5:55am figured it out
        # elif choice.lower() == 'q': # ------------------------------------------------------------------ REMOVED 5:55am not needed in main menu
        #     print("Exiting HouseMate. Have a great day!")
        #     status = False
        #     break  # Exit HouseMate when 'q' is entered
        else:
            print("Invalid choice. Please enter a number between 1 and 3 or 'q' to exit HouseMate.")

    if status == False: # ------------------------------------------------------------------------------------------ ADDED 5:55am figured it out
        break
    
    profile_menu_active = True # ------------------------------------------------------------------------------------------ ADDED 5:55am figured it out
    # Profile menu after successful login
    while profile_menu_active == True:
        profile_menu()
        choice = input("Enter your choice (1-5) or 'q' to exit HouseMate: ")

        if choice == '1':
            # View Profile Information
            view_profile(username, user_profiles)
            break # ------------------------------------------------------------------------------------------ ADDED 5:55am figured it out
        elif choice == '2':
            # Edit Profile
            edit_result, new_value = edit_profile(username, user_profiles)
            if edit_result == "username_changed":
                print("Username has been changed. Please login again.")
                #break # ------------------------------------------------------------------------------------------ REMOVED 5:55am figured it out
            elif edit_result == "password_changed":
                print("Password has been changed. Please login again.")
            break # ------------------------------------------------------------------------------------------ MOVED IN 1 INDENT 5:55am figured it out
        elif choice == '3':
            deleted_user = delete_profile(username, user_profiles)  # Utilize the decorated function
            if stringHash(username) == deleted_user:
                print("Profile has been deleted. Please log in again.")
            break  # Exit the menu loop when the user's profile is deleted # --------------------------------- MOVED IN 1 INDENT 5:55am figured it out
        elif choice == '4':
            housemate_menu_active = True
            while housemate_menu_active == True:
                housemate_menu() # ----------------------------------------------------------- might need to build out here --------
                choice = input("Enter your choice (1-5) or 'q' to exit HouseMate: ")

                if choice == '1':
                    # Find a home to rent or purchase based on recommendation parameters
                    print("This is *recommendation algorithm*?")
                    # rent_n = input("Enter the number of rental properties would you like to view: ")
                    # salary = input("Enter your approximate annual salary: ")
                    # downpay = input("Enter your approximate downpayment: ")
                    # pref_type = input("Enter the preferred type of property: ")
                    # pref_beds = input("Enter the preferred number of bedrooms: ")
                    continue # ------------------------------------------------------------------------------------------ ADDED 5:55am figured it out
                elif choice == '2':
                    # Find a home to rent
                    print("This is finding you a home to rent")
                    if __name__ == "__main__":
                        rental_main()
                    continue # ------------------------------------------------------------------------------------------ ADDED 5:55am figured it out
                elif choice == '3':
                    # Find a home to purchase
                    print("This is finding you a home to purchase")
                    if __name__ == "__main__":
                        purchase_main()
                    continue # ------------------------------------------------------------------------------------------ ADDED 5:55am figured it out
                elif choice == '4':
                    # Go back to main menu
                    print("This is returning to the profile menu")
                    housemate_menu_active = False # ------------------------------------------------------------------------------------------ ADDED 5:55am figured it out
                elif choice == '5':
                    # Logout
                    print("This is returning to the main menu.") # -------------------------------------------------------------- how to get back to first menu? big while loop?
                    housemate_menu_active = False # ------------------------------------------------------------------------------------------ ADDED 5:55am figured it out
                    profile_menu_active = False # ------------------------------------------------------------------------------------------ ADDED 5:55am figured it out
                elif choice.lower() == 'q':
                    print("Exiting HouseMate. Have a great day!")
                    status = False
                    housemate_menu_active = False
                    profile_menu_active = False
                    main_menu_active = False
                else:
                    print("Invalid choice. Please enter a number between 1 and 5 or 'q' to exit HouseMate.")
        elif choice == '5':
            # Logout and return to the main menu
            print("This is returning to the main menu.")
            break  # Exit the menu loop when logging out
        elif choice.lower() == 'q':
            print("Exiting HouseMate. Have a great day!")
            status = False
            break  # Exit HouseMate when 'q' is entered
        else:
            print("Invalid choice. Please enter a number between 1 and 5 or 'q' to exit HouseMate.")
    
    if status == False:
        break # Exit the outer while loop when the user chooses to exit HouseMate # ----------------------------------------------------------- ADDED 5:55am figured it out



# Save DataFrame to CSV
# Use hashed_username and hashed_password in the CSV
# save_dataframe_to_csv(existing_df, file_path)
# print("User Profile DataFrame:")
# print(existing_df)