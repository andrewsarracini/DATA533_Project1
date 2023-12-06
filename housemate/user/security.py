# security.py module

# Function to encrypt username and password credentials during profile creation
def string_hash(string):
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
    >>> string_hash("This is a test to see what happens")
    53286
    >>> string_hash("SensitiveInformationIsHere")
    33376
    >>> string_hash("What if there are numbers (333!) and symbols too?")
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
    >>> string_hash1 = "This is a test to see what happens"
    >>> string_hash2 = "SensitiveInformationIsHere"
    >>> string_hash3 = "What if there are numbers (333!) and symbols too?"

    >>> # Hash the strings and store them in the mapped_strings dictionary
    >>> hash_value_1 = string_hash(string_hash1)
    >>> hash_value_2 = string_hash(string_hash2)
    >>> hash_value_3 = string_hash(string_hash3)

    >>> mapped_strings[hash_value_1] = string_hash1
    >>> mapped_strings[hash_value_2] = string_hash2
    >>> mapped_strings[hash_value_3] = string_hash3

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

# Function to check credentials when logging in
def check_credentials(username, password, df):
    """
    Check the provided username and password against a DataFrame containing hashed credentials.

    Parameters
    ----------
    username : str
        The username provided by the user for login.

    password : str
        The password provided by the user for login.

    df : pandas.DataFrame
        A DataFrame containing stored usernames and passwords as hashed values.

    Returns
    -------
    bool
        True if the provided username and password match the hashed values stored in the DataFrame,
        False otherwise.

    Notes
    -----
    This function hashes the provided username and password, then checks for their presence
    in the DataFrame. It ensures both the username and password are in string format for
    comparison with the hashed values stored in the DataFrame.

    Examples
    --------
    >>> df = pd.DataFrame({
        'username': ['3337', '3345'],
        'password': ['3479', '3487']
    >>> })
    >>> check_credentials('username1', 'password1', df)
    True
    >>> check_credentials('username3', 'password3', df)
    False
    >>> check_credentials('username1', 'password3', df)
    False
    """
    if df is not None:
        # Hash the provided username and password
        hashed_username = str(string_hash(username))  # Convert the hashed values to strings
        hashed_password = str(string_hash(password))

        # Find matching profile using hashed username and password columns in DataFrame df
        matching_profile = df[(df['username'].astype(str) == hashed_username) & (df['password'].astype(str) == hashed_password)]
        return not matching_profile.empty

    return False


