# userlogin.py module

import pandas as pd
from security import stringHash, reverseHash, check_credentials
from userprofile import UserProfile, load_user_profiles, create_profile_from_input, append_to_dataframe, save_dataframe_to_csv

# Load user profiles from CSV file using load_user_profiles from userprofile.py module
file_path = r'C:\Users\cadla\OneDrive\Desktop\DATA533\Project\housemate\user\user_profiles.csv'
user_profiles = load_user_profiles(file_path)

# -------------------------------------------------------------------------------------------------------------------------------------------- functions start here ------------------------------------------

# Function to display main menu options ------------------------------- changed from display_menu to main_menu
def main_menu():
    print("Welcome to HouseMate! Choose an option:")
    print("1. Create Profile")
    print("2. Login")
    print("3. Exit")

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
    print("Choose an option:")
    print("1. Find a home to rent or purchase based on the recommendation parameters")
    print("2. Find a home to rent")
    print("3. Find a home to purchase")
    print("4. Go back to main menu")
    print("5. Logout")

# Function to view profile information
def view_profile(username, df):
    # Hash the username input
    hashed_username = stringHash(username)
    user_profile = df[df['username'] == hashed_username]
    if not user_profile.empty:
        print("Profile Information:")
        print(user_profile)
    else:
        print("No profile information found for this user.")

# Function to edit profile information
def edit_profile(username, df):
    new_value = None  # Placeholder for new_value within the function scope
    
    # Hash the username input
    hashed_username = stringHash(username)
    user_profile_index = df.index[df['username'] == hashed_username].tolist()
    
    if len(user_profile_index) > 0:
        field_to_edit = input("Enter the field to edit (name/age/email/username/password): ").lower()
        
        if field_to_edit in df.columns:
            new_value = input(f"Enter the new {field_to_edit}: ")

            # Conditional if/elif/else statement to exit the while loop menu when the username or password is changed ------------------------------- new addition important or else couldn't view/update further
            if field_to_edit == 'username':
                df.loc[user_profile_index[0], 'username'] = stringHash(new_value)
                save_dataframe_to_csv(df, file_path)  # Save to the specified location
                return "username_changed", new_value
            elif field_to_edit == 'password':
                df.loc[user_profile_index[0], 'password'] = stringHash(new_value)
                save_dataframe_to_csv(df, file_path)  # Save to the specified location
                return "password_changed", new_value
            else:
                df.loc[user_profile_index[0], field_to_edit] = new_value
                save_dataframe_to_csv(df, file_path)  # Save to the specified location
                print("Profile updated successfully!")
        else:
            print("Invalid field name. Profile not updated.")
    else:
        print("No profile information found for this user.")
    
    return "no_change", new_value  # Return new_value even if no change was made
        
# Function decorator for delete profile ------------------------------------------------ apply stringHash func to username so can call upon it later
def deleter(func):
    def wrapper(username, df):
        hashed_username = stringHash(username)
        user_profile_index = df.index[df['username'] == hashed_username].tolist()
        
        if len(user_profile_index) > 0:
            confirmation = input("Are you sure you want to delete your profile? (yes/no): ").lower()
            if confirmation == "yes":
                func(username, df)
                print("Profile deleted successfully!")
            else:
                print("Profile deletion canceled.")
        else:
            print("No profile information found for this user.")
        
        return hashed_username  # Return hashed username for use in the calling code
    return wrapper

# Function to delete profile information (decorated with deleter)
@deleter
def delete_profile(username, df):
    hashed_username = stringHash(username)
    user_profile_index = df.index[df['username'] == hashed_username].tolist()
    
    if len(user_profile_index) > 0:
        df.drop(user_profile_index, inplace=True)
        save_dataframe_to_csv(df, file_path)  # Save to the specified location
    else:
        print("No profile information found for this user.")

# -------------------------------------------------------------------------------------------------------------------------------------------------- functions end here ---------------------------------------

status = True

while status == True:
    main_menu()
    choice = input("Enter your choice (1-3) or 'q' to quit: ")
    
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
        while True:
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            if check_credentials(username, password, user_profiles):
                print("Login Successful!")
                break
            else:
                print("Invalid credentials. Please try again.")
        break
    elif choice == '3':
        print("Exiting HouseMate. Have a great day!")
        status = False
        break
    elif choice.lower() == 'q':
        print("Exiting menu. Goodbye!")
        status = False
        break  # Exit the menu loop when 'q' is entered
    else:
        print("Invalid choice. Please enter a number between 1 and 3 or 'q' to quit.")

# Display menu after successful login
while status == True:
    login_menu()
    choice = input("Enter your choice (1-5) or 'q' to quit: ")

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
        if True:
            housemate_menu() # ----------------------------------------------------------- might need to build out here --------
        else: continue
    elif choice == '5':
        # Logout
        print("Logging out. Goodbye!")
        break  # Exit the menu loop when logging out
    elif choice.lower() == 'q':
        print("Exiting menu. Goodbye!")
        break  # Exit the menu loop when 'q' is entered
    else:
        print("Invalid choice. Please enter a number between 1 and 5 or 'q' to quit.")



# Save DataFrame to CSV
# Use hashed_username and hashed_password in the CSV
# save_dataframe_to_csv(existing_df, file_path)
# print("User Profile DataFrame:")
# print(existing_df)