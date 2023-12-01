# security.py module

# ---------------- might add more functions here to save space elsewhere and organize/structure

# Function to anonymize username and password credentials during profile creation
def stringHash(string):
    """
    Returns a unique hashed value that references the string that it is applied to. The ordinal value 
    of each character in the string is modulus 9 and added for a total sum that is the resulting hash value. 
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
    176
    >>> stringHash("SensitiveInformationIsHere")
    96
    >>> stringHash("What if there are numbers and symbols too?")
    188
    """
    totalSum = 0
    mapping = {}
    for i, char in enumerate(string):
        totalSum += ord(char) * i
    mapping[totalSum] = string
    return totalSum

# Function to reverse the hashed values back into the original string
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
    >>> stringHash1 = "This is a test to see what happens"
    >>> stringHash2 = "SensitiveInformationIsHere"
    >>> stringHash3 = "What if there are numbers and symbols too?"

    >>> hash_value_1 = stringHash(stringHash1)
    >>> hash_value_2 = stringHash(stringHash2)
    >>> hash_value_3 = stringHash(stringHash3)

    >>> reverseHash(hash_value_1, mapped_strings)
    'This is a test to see what happens'

    >>> reverseHash(hash_value_2, mapped_strings)
    'SensitiveInformationIsHere'

    >>> reverseHash(hash_value_3, mapped_strings)
    'What if there are numbers and symbols too?'

    >>> reverseHash(999, mapped_strings)
    None
    """
    if mapped_values is None:
        mapped_values = {}

    return mapped_values.get(hash_value)

# Function to check credentials when logging in
def check_credentials(username, password, df):
    if df is not None:
        # Reverse the user input using stringHash function
        reversed_username = stringHash(username)
        reversed_password = stringHash(password)

        # Find matching profile using reversed username and password
        matching_profile = df[(df['username'] == reversed_username) & (df['password'] == reversed_password)]
        return not matching_profile.empty
    return False
