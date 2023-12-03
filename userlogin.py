# userlogin.py module

import pandas as pd
from security import stringHash, reverseHash, check_credentials
from userprofile import load_user_profiles, save_dataframe_to_csv

# Load user profiles from CSV file using load_user_profiles from userprofile.py module
file_path = r'C:\Users\cadla\OneDrive\Desktop\DATA533\Project\housemate\user\user_profiles.csv'
user_profiles = load_user_profiles(file_path)

# -------------------------------------------------------------------------------------------------------------------------------------------- functions start here

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

# -------------------------------------------------------------------------------------------------------------------------------------------------- functions stop here



