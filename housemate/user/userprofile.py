# userprofile.py module

import os
import pandas as pd
from security import stringHash

# UserProfile class
class UserProfile:

    def __init__(self, profile_data):
        self.name = profile_data.get('name')
        self.age = profile_data.get('age')
        self.email = profile_data.get('email')
        self.username = profile_data.get('username')
        self.password = profile_data.get('password')

    def get_profile_info(self):
        return f"Name: {self.name}, Age: {self.age}, Email: {self.email}, Username: {self.username}"

# Function to create a new profile based on user input
def create_profile_from_input():
    profile_data = {}
    profile_data['name'] = input("Enter your name: ")
    profile_data['age'] = int(input("Enter your age: "))
    profile_data['email'] = input("Enter your email: ")
    profile_data['username'] = input("Enter your username: ")
    profile_data['password'] = input("Enter your password: ")

    # Hash the username and password before storing
    profile_data['username'] = stringHash(profile_data['username'])
    profile_data['password'] = stringHash(profile_data['password'])

    return profile_data

# Function to add profile information to a dataframe
def append_to_dataframe(df, user_profile_data):
    new_df = pd.DataFrame([user_profile_data])
    if df is None:
        df = new_df
    else:
        df = pd.concat([df, new_df], ignore_index=True)
    return df

# Function to load the CSV file that holds the user profiles
def load_user_profiles(file_path):
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    return None

# Function to save the user profiles in the dataframe to a CSV file
def save_dataframe_to_csv(df, file_path):
    df.to_csv(file_path, index=False)

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


