# userlogin.py module

import pandas as pd
from security import stringHash, reverseHash
from userprofile import load_user_profiles, save_dataframe_to_csv

# Function to display menu options
def display_menu():
    print("Welcome! Choose an option:")
    print("1. View Profile Information")
    print("2. Edit Profile")
    print("3. Delete Profile")
    print("4. View Messages")
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
    # Hash the username input
    hashed_username = stringHash(username)
    user_profile_index = df.index[df['username'] == hashed_username].tolist()
    if len(user_profile_index) > 0:
        field_to_edit = input("Enter the field to edit (name/age/email/username/password): ").lower()
        if field_to_edit in df.columns:
            new_value = input(f"Enter the new {field_to_edit}: ")

            # Update the DataFrame with the modified profile data
            df.loc[user_profile_index[0], field_to_edit] = new_value
            save_dataframe_to_csv(df, file_path)  # Save to the specified location
            
            print("Profile updated successfully!")
        else:
            print("Invalid field name. Profile not updated.")
    else:
        print("No profile information found for this user.")
        
# Function decorator for delete profile
def deleter(func):
    def wrapper(username, df):
        user_profile_index = df.index[df['username'] == username].tolist()
        if len(user_profile_index) > 0:
            confirmation = input("Are you sure you want to delete your profile? (yes/no): ").lower()
            if confirmation == "yes":
                func(username, df)
                print("Profile deleted successfully!")
            else:
                print("Profile deletion canceled.")
        else:
            print("No profile information found for this user.")
    return wrapper

# Function to delete profile information (decorated with deleter)
@deleter
def delete_profile(username, df):
    # Remove the profile from the DataFrame
    user_profile_index = df.index[df['username'] == username].tolist()
    df.drop(user_profile_index, inplace=True)
    save_dataframe_to_csv(df, file_path)  # Save to the specified location

# Load user profiles from CSV file using load_user_profiles from userprofile.py module
file_path = r'C:\Users\cadla\OneDrive\Desktop\DATA533\Project\housemate\user\user_profiles.csv'
user_profiles = load_user_profiles(file_path)

# Function to check credentials when logging in ---------------------------------------------------- might move to security to save space & organize/structure
def check_credentials(username, password, df):
    if df is not None:
        # Reverse the user input using stringHash function
        reversed_username = stringHash(username)
        reversed_password = stringHash(password)

        # Find matching profile using reversed username and password
        matching_profile = df[(df['username'] == reversed_username) & (df['password'] == reversed_password)]
        return not matching_profile.empty
    return False

# While loop to take in the username and password and match to credentials stored in CSV, if no match continues asking --------------------- might need to add an escape
while True:
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if check_credentials(username, password, user_profiles):
        print("Login Successful!")
        break
    else:
        print("Invalid credentials. Please try again.")

# Display menu after successful login
while True:
    display_menu()
    choice = input("Enter your choice (1-5) or 'q' to quit: ")

    if choice == '1':
        # View Profile Information
        view_profile(username, user_profiles)
    elif choice == '2':
        # Edit Profile
        edit_profile(username, user_profiles)
    elif choice == '3':
        # Delete Profile
        delete_profile(username, user_profiles)  # Utilize the decorated function
    elif choice == '4':
        # View Available Homes -------------------------------------------------------- incorporate other subpackage here
        print("View available homes...")
    elif choice == '5':
        # Logout
        print("Logging out. Goodbye!")
        break  # Exit the menu loop when logging out
    elif choice.lower() == 'q':
        print("Exiting menu. Goodbye!")
        break  # Exit the menu loop when 'q' is entered
    else:
        print("Invalid choice. Please enter a number between 1 and 5 or 'q' to quit.")


