DATA533_Project_HouseMate

The HouseMate package has 2 sub-packages, which are user and property. The user sub-package contains 3 modules; userprofile.py, userlogin.py and security.py, while the property sub-package also contains 3 modules; property.py, purchase.py and rental.py. Finally, there is a standalone module called housemate.py which imports all the modules and houses the logic to make the various menus and functions flow correctly. 

HouseMate/
├── __init__.py
├── housemate.py        
├── user/               
│   ├── __init__.py
│   ├── userprofile.py  
│   ├── userlogin.py    
│   └── security.py     
└── property/           
    ├── __init__.py
    ├── property.py     
    ├── purchase.py     
    └── rental.py       

## Sub-Class: Property
#### property.py 
Contains the superclass Property, which instantiates various attributes for all inherited property types. 
Attributes include: 
- sqft (the amount of square footage)
- num_beds (number of bedrooms)
- num_baths (the number of bathrooms)

#### purchase.py
Contains the subclass Purchase, which inherits from Property. Purchase functions to instantiate additional attributes that pertain to all Purchase-type objects. 
Attributes include: 
- price (the cost of acquiring the property)
- mortgage_term (the number of years on the mortgage)
- interest (the interest rate factored into the mortgage calculation)

Purchase contains 2 methods:
- `calculate_mortgage` -- uses Purchase-type attributes and user input to calculate a suitable mortgage for any type of Purchase property.
- `display` -- An overview of the object's attributes with informative print statements and all calculations in one place

Purchase contains 3 functions: 
- `gen_purchase` -- generates n amount (user controlled) of Purchase-type properties in a list
- `purchase_recommendation` -- considers user parameters, such as downpayment, income and home preferences in order to match the user with Purchase properties that fit their specifications
- `view_purchase_list` -- backgruond function that facilitates easy viewing of the recommendation list, along with some quality-of-life display enhancements for user satisfaction. 

Finally, purchase.py also contains 6 subclasses, all of which inherit from Purchase. These subclasses each align with a different type of Purchase-property, which are differentiated by randomly generating their attributes within finely-tuned numerical ranges. This is done by setting their attribute values to random.randint(x, y) in each subclass __init__ call, so the objects are automatically randomized (within a range) as they are created. 
Subclasses of Purchase: 
- Condo
- TownHome
- Duplex
- Bungalow
- TwoStory
- Mansion

#### rental.py
Contains the subclass Rental, which inherits from Property. Rental functions to instantiate additional attributes that pertain to all Rental-type objects. 
Attributes include: 
- rent (the base cost per month for this property)
- utilities (expenses often required for renting individuals by landlords) 
- lease_term (the length of months that the lease agreenment is good for)
- pet (whether or not a pet is present in the Rental unit, which will require a pet deposit)

Rental contains 2 methods: 
- `calc_total_rent` -- calculates total rent based on rent, utilities and lease term
- `display_rental` -- an overview of the object's attributes with informative print statements and all calculations in one place

Rental contains 3 functions:
- `gen_rental` -- generates n amount (user controlled) of Rental-type properties in a list
- `rental_recommendation` -- considers user parameters, such as income and home preferences in order to match the user with Rental properties that fit their specifications
- `view_rental_list` -- backgruond function that facilitates easy viewing of the recommendation list, along with some quality-of-life display enhancements for user satisfaction. 

Finally, rental.py also contains 6 subclasses, all of which inherit from Rental. These subclasses each align with a different type of Rental-property, which are differentiated by randomly generating their attributes within finely-tuned numerical ranges. This is done by setting their attribute values to random.randint(x, y) in each subclass __init__ call, so the objects are automatically randomized (within a range) as they are created. 
Subclasses of Rental: 
- RentalCondo
- RentalTownHome
- RentalDuplex
- RentalBungalow
- RentalTwoStory
- RentalMansion

## Sub-Class: User
#### userprofile.py
The userprofile.py module allows the user to create their profile by entering their name, age and email, as well as their chosen username and password. The username and password are encrypted using a hash function (from security.py) in order to be stored as a hash value for privacy and security reasons. There is a class UserProfile that instantiates each of the attributes (i.e, name, age etc.) and allows for retrieval from secure storage in the .csv file. 
 
- `load_user_profiles` -- used to load the user profiles, which are stored in a CSV file locally. If there is no `file_path` to the CSV file, none will be returned
- `create_profile_from_input` -- used to create the profile for the user based on user input. The following restrictions are in place:
- `age_input` -- must be between 11 and 999 and an integer only
- `email` -- using regular expressions to form a defined pattern, there must be alphanumeric characters before the @ symbol as well as in between @ and .com
- `username` -- must be between 8 and 33 characters without the use of spaces
- `password` -- must be between 8 and 133 characters without the use of spaces
- `append_to_dataframe` -- used to concatenate the new user defined attributes into a dataframe. If there is no dataframe, there will be one created.
- `save_dataframe_to_csv` -- used to save the dataframe that was created and/or concatenated to, and be saved locally as per the `file_path`
 
#### userlogin.py
This module allows the user to login with their created credentials by entering their username and password. These credentials are then encrypted with a hash function to be matched with the hash values that were stored after creating the profile. 
 
- `login_get_file_path` -- used to determine the `file_path` in which the `user_profiles.csv` file will be stored
- `view_profile` -- used to allow the user to view the profile that they have created in the form of a dataframe with only their profile attributes (i.e., name, age etc.), in which the username and password are displayed as the corresponding hash value
- `edit_profile` -- used to allow the user to edit attributes in the profile by allowing them to select which attribute to edit. If either the username or password are edited, the user is exited to the main menu to login with the newly created credentials
- `delete_profile` -- used to allow the user to delete their profile completely from the dataframe and CSV, in which they are exited from the profile menu to the main menu

#### security.py
The security.py module ensures that the sensitive user attributes, such as username and password, are encrypted using a hash function as well as checked when logging in.
 
- `stringHash` -- takes in the username and password strings, which are then enumerated and multiplied by the corresponding ordinal value for each character to equal a single, summed hash value
- `reverseHash` -- takes in the hashed values for username and password to be reversed into the original string in case of forgotten usernames or passwords (on the back end)
- `check_credentials` -- utilizes the `stringHash` function above to convert the entered login credentials (i.e., username and password) into the corresponding hash value to be matched with the hash value stored in the CSV

## Standalone Module: 
#### housemate.py
This module imports from both Property and User sub-packages, and acts as a staging ground for the HouseMate application as a whole. This module mainly does this through housing the multitude of menus required, gathering functions and allowing them to work in concert. 
Main functionalities include: 
- Menu management and control of flow, applies to: 
  - user profile functionalities
  - authentication 
  - Property viewing
  - Property recommending
 
There are many functions within housemate.py that allow for flow including: 
- Menu functions: allow for users to select options based on prompts
   - `main_menu`, `profile_menu`, `housemate_menu`
- Mapping functions: allow for user-friendly input 
   - `purchase_main`, `rental_main`, `purchase_recommendation_main`, `renatl_recommendation_main`
 
- Also note, housemate.py protects against all user input from invalid characters and character lengths. In the case of email, only a certain pattern will be accepted ("example@email.com") 

**Final notes:**
Known bug: currently we have an issue where the login system is not accepting new users due to the .csv file not being properly created in the file_path. This will prevent any user from entering into HouseMate the intended way, but by "failing" to log in 3 times, the next set of menus is accessible. This is not an intended part of the HouseMate and we are working on a fix. 

