# userlogin.py module

import os
import pandas as pd
from .security import stringHash, reverseHash, check_credentials
from .userprofile import load_user_profiles, save_dataframe_to_csv

# Function to establish file_path and load user profiles from CSV file using load_user_profiles from userprofile.py module
def login_get_file_path():
    # Using a relative path (will stored in the user's home directory)
    relative_path = 'user/user_profiles.csv'
    if os.path.exists(relative_path):
        return relative_path

    # If the file is not found, return a default path in the user's home directory
    home_dir = os.path.expanduser('~')
    default_path = os.path.join(home_dir, 'user_profiles.csv')
    return default_path

file_path = login_get_file_path()
user_profiles = load_user_profiles(file_path)

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
    new_value = None # Placeholder for new_value within the function scope
    
    # Hash the username input
    hashed_username = stringHash(username)
    user_profile_index = df.index[df['username'] == hashed_username].tolist()
    
    if len(user_profile_index) > 0:
        field_to_edit = input("Enter the field to edit (name/age/email/username/password): ").lower()
        
        if field_to_edit in df.columns:
            new_value = input(f"Enter the new {field_to_edit}: ")

            # Conditional if/elif/else statement to exit the while loop menu when the username or password is changed (to re login)
            if field_to_edit == 'username':
                df.loc[user_profile_index[0], 'username'] = stringHash(new_value)
                save_dataframe_to_csv(df, file_path) # Save to the specified location
                return "username_changed", new_value
            elif field_to_edit == 'password':
                df.loc[user_profile_index[0], 'password'] = stringHash(new_value)
                save_dataframe_to_csv(df, file_path) # Save to the specified location
                return "password_changed", new_value
            else:
                df.loc[user_profile_index[0], field_to_edit] = new_value
                save_dataframe_to_csv(df, file_path) # Save to the specified location
                print("Profile updated successfully!")
        else:
            print("Invalid field name. Profile not updated.")
    else:
        print("No profile information found for this user.")
    
    return "no_change", new_value # Return new_value even if no change was made
        
# Function decorator for delete profile
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
        
        return hashed_username # Return hashed username for use in the calling code
    return wrapper

# Function to delete profile information (decorated with deleter)
@deleter
def delete_profile(username, df):
    hashed_username = stringHash(username)
    user_profile_index = df.index[df['username'] == hashed_username].tolist()
    
    if len(user_profile_index) > 0:
        df.drop(user_profile_index, inplace=True)
        save_dataframe_to_csv(df, file_path) # Save to the specified location
    else:
        print("No profile information found for this user.")


