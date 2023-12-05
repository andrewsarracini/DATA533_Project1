import random

# Superclass Property


class Property(object):
    def __init__(self, sqft, num_beds, num_baths):
        self.sqft = sqft
        self.num_beds = num_beds
        self.num_baths = num_baths

    def display_property(self):
        print(f'The price of this property is: ${self.price}.00')
        print(f'The square footage of this property is: {self.sqft} ft.')
        print(f'This property has {self.num_beds} bedrooms')
        print(f'This property has {self.num_baths} bathrooms')


# prop_list = []


# def gen_n_properties(n):
#     for i in range(n):
#         prop_list.append(Property())
#         print(f'Property {i} created')


# Note: p1 = Person() # autofills all attributes thanks to second __init__

# example: gen_n_properties(3)
# output: Property 0 created
# Property 1 created
# Property 2 created
# Now we can reference prop_list[i].display_property


# Problems:
# It generates truly random properties--
# Meaning it can give a house for $300,000 and 44999 sqft, but only 2 bed and 1 bath
# Secondly, price doesn't belong in Property (it belongs in Purchase) --
# I realized that once it was already in, but it's an easy copy + paste
# More to come!
