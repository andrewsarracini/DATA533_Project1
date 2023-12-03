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

# Function to load the CSV file that holds the user profiles ------------------------------------------------------------------------ moved to top
def load_user_profiles(file_path):
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    return None

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

# Function to save the user profiles in the dataframe to a CSV file
def save_dataframe_to_csv(df, file_path):
    df.to_csv(file_path, index=False)


