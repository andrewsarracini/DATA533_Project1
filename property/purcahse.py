import property
import random


class Purchase(Property):
    def __init__(self, sqft, num_beds, num_baths, price, mortgage, interest):
        super().__init__(sqft, num_beds, num_baths)
        self.price = price  # subclass-specific random generation instead of here
        self.mortgage = mortgage  # subclass-specific random generation instead of here
        self.interest = interest


class Condo(Purchase):
    def __init__(self, sqft, num_beds, num_baths, price, mortgage):
        super().__init__(sqft, num_beds, num_baths, price, mortgage)

    def __init__(self):
        self.sqft = random.randint(350, 800)
        self.num_beds = 1
        self.num_baths = 1
        self.price = random.randint(300000, 500000)
        self.mortgage = random.randint(800, 6000)

    def display_condo(self):
        print(f'The price of this condo is: ${self.price}.00')
        print(f'The mortgage on this condo is ${self.mortgage}.00 per month')
        print(f'The square footage of this condo is: {self.sqft} ft.')
        print(f'This condo has {self.num_beds} bedrooms')
        print(f'This condo has {self.num_baths} bathrooms')

    # def __repr__(self):
    #     return (f'Condo price: ${self.price}.00 \n'
    #             f'Condo monthly mortgage: ${self.mortgage}.00 \n'
    #             f'Condo square footage: {self.sqft} ft. \n'
    #             f'Condo bedrooms: {self.num_beds} \n'
    #             f'Condo bathrooms: {self.num_baths}')


prop_list = []


def gen_props(n, prop_type):
    for i in range(n):
        prop_list.append(prop_type)
        print(f'Property Type: {prop_type} {i} created')
