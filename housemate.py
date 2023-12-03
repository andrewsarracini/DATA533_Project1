# housemate.py module

import pandas as pd
from security import stringHash, reverseHash, check_credentials
from userprofile import UserProfile, load_user_profiles, create_profile_from_input, append_to_dataframe, save_dataframe_to_csv
from userlogin import view_profile, edit_profile, delete_profile

# Load user profiles from CSV file using load_user_profiles from userprofile.py module
file_path = r'C:\Users\cadla\OneDrive\Desktop\DATA533\Project\housemate\user\user_profiles.csv'
user_profiles = load_user_profiles(file_path)

# -------------------------------------------------------------------------------------------------------------------------------------------- functions start here ------------------------------------------

# Function to display main menu options ------------------------------- changed from display_menu to main_menu
def main_menu():
    print("Welcome to HouseMate! Choose an option:")
    print("1. Create Profile")
    print("2. Login")
    print("3. Exit HouseMate")

# Function to display login menu options
def login_menu():
    print("Thanks for logging in! Choose an option:")
    print("1. View Profile Information")
    print("2. Edit Profile")
    print("3. Delete Profile")
    print("4. View available homes")
    print("5. Logout")
    
# Function to display the housemate menu options --------------------- added ---------------
def housemate_menu(): 
    print("Find a home today! Choose an option:")
    print("1. Find a home to rent or purchase based on the recommendation parameters")
    print("2. Find a home to rent")
    print("3. Find a home to purchase")
    print("4. Go back to main menu")
    print("5. Logout")

# -------------------------------------------------------------------------------------------------------------------------------------------------- functions end here ---------------------------------------

status = True # added to exit from HouseMate during while loops ------------------------------ CHANGED

while status == True:
    main_menu()
    choice = input("Enter your choice (1-3) or 'q' to exit HouseMate: ")
    
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

    elif choice == '3':
        print("Exiting HouseMate. Have a great day!")
        status = False
        break
    elif choice.lower() == 'q':
        print("Exiting HouseMate. Have a great day!")
        status = False
        break  # Exit HouseMate when 'q' is entered
    else:
        print("Invalid choice. Please enter a number between 1 and 3 or 'q' to exit HouseMate.")

# Display menu after successful login
while status == True:
    login_menu()
    choice = input("Enter your choice (1-5) or 'q' to exit HouseMate: ")

    if choice == '1':
        # View Profile Information
        view_profile(username, user_profiles)
    elif choice == '2':
        # Edit Profile
        edit_result, new_value = edit_profile(username, user_profiles)
        if edit_result == "username_changed":
            print("Username has been changed. Please login again.")
            break
        elif edit_result == "password_changed":
            print("Password has been changed. Please login again.")
            break
    elif choice == '3':
        deleted_user = delete_profile(username, user_profiles)  # Utilize the decorated function
        if stringHash(username) == deleted_user:
            print("Profile has been deleted. Please log in again.")
            break  # Exit the menu loop when the user's profile is deleted ------------------------------ added ------------
    elif choice == '4':
        while True:
            housemate_menu() # ----------------------------------------------------------- might need to build out here --------
            choice = input("Enter your choice (1-5) or 'q' to exit HouseMate: ")

            if choice == '1':
                # Find a home to rent or purchase based on recommendation parameters
                print("This is finding a home to rend or buy based on recommendations")
            elif choice == '2':
                # Find a home to rent
                print("This is finding a home to rent")
            elif choice == '3':
                # Find a home to purchase
                print("This is finding a home to purchase")
            elif choice == '4':
                # Go back to main menu
                print("This is going back to the previous menu")
            elif choice == '5':
                # Logout
                print("Logging out. Goodbye!")
                break  # Exit the menu loop when logging out
            elif choice.lower() == 'q':
                print("Exiting HouseMate. Have a great day!")
                status = False
                break  # Exit HouseMate when 'q' is entered
            else:
                print("Invalid choice. Please enter a number between 1 and 5 or 'q' to exit HouseMate.")
    elif choice == '5':
        # Logout
        print("Logging out. Goodbye!")
        break  # Exit the menu loop when logging out
    elif choice.lower() == 'q':
        print("Exiting HouseMate. Have a great day!")
        break  # Exit HouseMate when 'q' is entered
    else:
        print("Invalid choice. Please enter a number between 1 and 5 or 'q' to exit HouseMate.")



# Save DataFrame to CSV
# Use hashed_username and hashed_password in the CSV
# save_dataframe_to_csv(existing_df, file_path)
# print("User Profile DataFrame:")
# print(existing_df)