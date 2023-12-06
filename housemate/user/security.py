# security.py module

# Function to encrypt username and password credentials during profile creation
def stringHash(string):
    """
    Returns a unique hashed value that references the string that it is applied to. 
    The ordinal value of each character in the string is multiplied by its enumerated 
    value and added for a total sum that is the resulting hash value. 
    Can be reversed.
    
    Parameters
    ----------
    string : a string value or list of string values
        
    Returns
    -------
    integer
        An integer that contains the resulting integer hash value that represents the string input.
        
    Examples
    --------
    >>> stringHash("This is a test to see what happens")
    53286
    >>> stringHash("SensitiveInformationIsHere")
    33376
    >>> stringHash("What if there are numbers (333!) and symbols too?")
    101197
    """
    totalSum = 0
    mapping = {}
    for i, char in enumerate(string):
        totalSum += ord(char) * i
    mapping[totalSum] = string
    return totalSum

# Function to reverse the hashed values back into the original string 
# (for use on the back end if needed; e.g., forgot username, password etc.)
def reverseHash(hash_value, mapped_values):
    """
    Reverses the hashed value back to its original string representation.

    Parameters
    ----------
    hash_value : int
        An integer representing the hashed value.
    mapped_values : dict
        A dictionary containing hashed values as keys and their respective strings as values.

    Returns
    -------
    str or None
        The original string if found in the mapped_values dictionary, otherwise None.

    Examples
    --------
    >>> mapped_strings = {}

    >>> # Hashing the strings
    >>> stringHash1 = "This is a test to see what happens"
    >>> stringHash2 = "SensitiveInformationIsHere"
    >>> stringHash3 = "What if there are numbers (333!) and symbols too?"

    >>> # Hash the strings and store them in the mapped_strings dictionary
    >>> hash_value_1 = stringHash(stringHash1)
    >>> hash_value_2 = stringHash(stringHash2)
    >>> hash_value_3 = stringHash(stringHash3)

    >>> mapped_strings[hash_value_1] = stringHash1
    >>> mapped_strings[hash_value_2] = stringHash2
    >>> mapped_strings[hash_value_3] = stringHash3

    >>> # Now perform the reverse lookup
    >>> result_1 = reverseHash(hash_value_1, mapped_strings)
    >>> result_2 = reverseHash(hash_value_2, mapped_strings)
    >>> result_3 = reverseHash(hash_value_3, mapped_strings)

    >>> print(result_1)  # Output: This is a test to see what happens
    "This is a test to see what happens"
    >>> print(result_2)  # Output: SensitiveInformationIsHere
    "SensitiveInformationIsHere"
    >>> print(result_3)  # Output: What if there are numbers (333!) and symbols too?
    "What if there are numbers (333!) and symbols too?"
    """
    
    if mapped_values is None:
        mapped_values = {}

    return mapped_values.get(hash_value)

# Function to check credentials when logging in by matching the hashed values of 
# the user input to the hashed values that are stored in the CSV
# Function to check credentials when logging in
def check_credentials(username, password, df):
    """
    Verifies the input username and password by reversing and hashing the provided 
    credentials and matching them with the hashed values stored in a CSV file.

    Parameters
    ----------
    username : str
        The username provided by the user.

    password : str
        The password provided by the user.

    hashed_credentials : dict
        A dictionary containing hashed usernames and passwords as keys and their respective 
        original values as values.

    Returns
    -------
    bool
        True if the provided username and password match the hashed values stored in the CSV, 
        False otherwise.

    Examples
    --------
    >>> hashed_credentials = {
    ...     stringHash("user1"): stringHash("password1"),
    ...     stringHash("user2"): stringHash("password2"),
    ...     stringHash("user3"): stringHash("password3"),
    ... }
    >>> check_credentials("user1", "password1", hashed_credentials)
    True
    >>> check_credentials("user2", "wrong_password", hashed_credentials)
    False
    >>> check_credentials("non_existing_user", "password123", hashed_credentials)
    False
    """
    # Implement the logic to check the credentials against the hashed values
    # Retrieve the hashed values of the provided username and password

# Function to check credentials when logging in
def check_credentials(username, password, df):
    if df is not None:
        # Hash the provided username and password
        hashed_username = stringHash(username)
        hashed_password = stringHash(password)

        # Find matching profile using hashed username and password columns in DataFrame df
        matching_profile = df[(df['username'] == hashed_username) & (df['password'] == hashed_password)]
        print(hashed_password)
        print(df['password'])
        print(hashed_username)
        print(df['username'])
        return not matching_profile.empty
    print("False here")
    return False

# Function to check credentials when logging in
# def check_credentials(username, password, df):
#     if df is not None:
#         # Hash the provided username and password
#         hashed_username = stringHash(username)
#         hashed_password = stringHash(password)

#         # Convert hashed values to the same data type as stored in DataFrame (e.g., strings)
#         hashed_username = str(hashed_username)
#         hashed_password = str(hashed_password)

#         # Strip any leading or trailing whitespace
#         hashed_username = hashed_username.strip()
#         hashed_password = hashed_password.strip()

#         # Find matching profile using hashed username and password columns in DataFrame df
#         matching_profile = df[(df['username'].str.strip() == hashed_username) & (df['password'].str.strip() == hashed_password)]
#         return not matching_profile.empty

#     return False


# ------------------------ for debugging ------------------ they match
# Function to check credentials when logging in
# def check_credentials(username, password, df):
#     if df is not None:
#         # Hash the provided username and password
#         hashed_username = stringHash(username)
#         hashed_password = stringHash(password)

#         # Find matching profile using hashed username and password columns in DataFrame df
#         matching_profile = df[(df['username'] == hashed_username) & (df['password'] == hashed_password)]

#         print("Hashed Username (Input):", hashed_username)
#         print("Hashed Password (Input):", hashed_password)
#         print("DataFrame Username:", df['username'])
#         print("DataFrame Password:", df['password'])
#         print("Matching Profile:", matching_profile)

#         return not matching_profile.empty

#     return False

# ------------------------ for debugging ------------------ they match not sure why it won't work
# Hashed Username (Input): 6023
# Hashed Password (Input): 6023
# DataFrame Username: 0              3914
# 1              3914
# 2              3846
# 3              4484
# 4              4376
# 5              5395
# 6     usernamedebug
# 7     usernamedebug
# 8     usernamedebug
# 9     usernamedebug
# 10        debugging
# 11             5509
# 12             3919
# 13             3871
# 14             4241
# 15             4304
# 16             4895
# 17             4975
# 18             5475
# 19             4992
# 20             5798
# 21             4347
# 22             7214
# 23             4782
# 24             7135
# 25             8715
# 26             9365
# 27             6899
# 28             6131
# 29            15123
# 30             7206
# 31             3936
# 32             3504
# 33             4548
# 34             7540
# 35             5799
# 36             4246
# 37             4264
# 38             4827
# 39             4273
# 40             3491
# 41             9783
# 42             4832
# 43             6023
# Name: username, dtype: object
# DataFrame Password: 0              4056
# 1              4056
# 2              3988
# 3              4626
# 4              4518
# 5              5537
# 6     passworddebug
# 7     passworddebug
# 8     passworddebug
# 9     passworddebug
# 10        debugging
# 11             5509
# 12             3919
# 13             3871
# 14             4383
# 15             4304
# 16             4895
# 17             4975
# 18             5475
# 19             4992
# 20             5798
# 21             4489
# 22             7214
# 23             4782
# 24             7135
# 25             8715
# 26             9365
# 27             7278
# 28             6131
# 29            15123
# 30             7206
# 31             3936
# 32             3504
# 33             4548
# 34             7540
# 35             5799
# 36             4246
# 37             4264
# 38             4827
# 39             4273
# 40             3491
# 41            10039
# 42             4832
# 43             6023
# Name: password, dtype: object
# Matching Profile: Empty DataFrame
# Columns: [name, age, email, username, password]
# Index: []
# Invalid credentials. 2 attempts remaining.