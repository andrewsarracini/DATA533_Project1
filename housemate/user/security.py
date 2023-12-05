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
def check_credentials(username, password, hashed_credentials):
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
    hashed_username = stringHash(username)
    hashed_password = stringHash(password)

    # Check if the hashed values match the stored credentials
    return hashed_credentials.get(hashed_username) == hashed_password


