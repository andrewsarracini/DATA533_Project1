# userprofile.py module

import os
import re
import pandas as pd
from .security import stringHash

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

# Function to load the CSV file that holds the user profiles
def load_user_profiles(file_path):
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    return None

# Function to create a new profile based on user input with validation for age, email, username, and password
def create_profile_from_input():
    profile_data = {}
    profile_data['name'] = input("Enter your name: ")

    while True:
        age_input = input("Enter your age: ")
        if age_input.isdigit():
            age = int(age_input)
            if 11 <= age <= 999:
                profile_data['age'] = age
                break
            else:
                print("Invalid age. Please enter an integer between 11 and 999.")
        else:
            print("Invalid input. Please enter a valid integer for age.")

    while True:
        while True:
            email = input("Enter your email: ")
            # Remove leading and trailing spaces for validation
            email = email.strip()

            # Regular expression pattern for email validation
            email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

            if email and re.match(email_pattern, email):
                profile_data['email'] = email
                break
            else:
                print("Invalid email format or empty input. Please enter a valid email address.")

        while True:
            username = input("Enter your username (8 characters or more): ")
            if ' ' not in username and 8 <= len(username) <= 33:
                profile_data['username'] = username
                break
            else:
                if ' ' in username:
                    print("Invalid username. Please avoid spaces in the username.")
                else:
                    print("Username should be between 8 and 33 characters.")

        while True:
            password = input("Enter your password (8 characters or more): ")
            if ' ' not in password and 8 <= len(password) <= 133:
                profile_data['password'] = password
                break
            else:
                if ' ' in password:
                    print("Invalid password. Please avoid spaces in the password.")
                else:
                    print("Password should be between 8 and 133 characters.")

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

