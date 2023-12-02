from property import Property
import random


class Rental(Property):
    def __init__(self, sqft, num_beds, num_baths, rent, utilities, lease_term=12, pet=False):
        super().__init__(sqft, num_beds, num_baths)
        self.rent = rent
        self.utilities = utilities
        self.lease_term = lease_term
        self.pet = pet

    def calc_total_rent(self):
        pet_deposit = 0
        if self.pet:
            # Pet deposit requires user input -- Rental differs in this way from Purchase
            pet_deposit = 500
        total = self.lease_term * (self.rent + self.utilities) + pet_deposit
        return total

    def display_rental(self):
        class_name = type(self).__name__
        print(f'Rental type: {class_name}')
        print(f'Monthly rent: ${self.rent}')
        print(f'Monthly utilities: ${self.utilities}')
        print(f'Pet deposit required: {self.pet}')
        print(f'Annual total: ${self.calc_total_rent()}')
        print(f'Square footage: {self.sqft}sqft.')
        print(f'Number of bedrooms: {self.num_beds}')
        print(f'Number of bathrooms: {self.num_baths}')


class RentalCondo(Rental):
    def __init__(self):
        sqft = random.randint(350, 850)
        num_beds = random.randint(1, 2)
        num_baths = 1
        rent = random.randint(1200, 1800)
        utilities = random.randint(100, 150)
        super().__init__(sqft, num_beds, num_baths, rent, utilities)


class RentalTownHome(Rental):
    def __init__(self):
        sqft = random.randint(800, 1800)
        num_beds = random.randint(2, 4)
        num_baths = random.randint(1, 3)
        rent = random.randint(1900, 2800)
        utilities = random.randint(200, 250)
        super().__init__(sqft, num_beds, num_baths, rent, utilities)


class RentalDuplex(Rental):
    def __init__(self):
        sqft = random.randint(1000, 2000)
        num_beds = random.randint(2, 5)
        num_baths = random.randint(2, 4)
        rent = random.randint(2400, 3300)
        utilities = random.randint(250, 300)
        super().__init__(sqft, num_beds, num_baths, rent, utilities)


class RentalBungalow(Rental):
    def __init__(self):
        sqft = random.randint(1300, 2400)
        num_beds = random.randint(4, 5)
        num_baths = random.randint(3, 4)
        rent = random.randint(3200, 4400)
        utilities = random.randint(300, 400)
        super().__init__(sqft, num_beds, num_baths, rent, utilities)


class RentalTwoStory(Rental):
    def __init__(self):
        sqft = random.randint(2000, 3300)
        num_beds = random.randint(4, 6)
        num_baths = random.randint(3, 5)
        rent = random.randint(4200, 5500)
        utilities = random.randint(350, 450)
        super().__init__(sqft, num_beds, num_baths, rent, utilities)


class RentalMansion(Rental):
    def __init__(self):
        sqft = random.randint(5000, 12000)
        num_beds = random.randint(8, 10)
        num_baths = random.randint(7, 8)
        rent = random.randint(10000, 13000)
        utilities = random.randint(500, 675)
        super().__init__(sqft, num_beds, num_baths, rent, utilities)


rental_list = []


def gen_rental(n, prop_type):
    for i in range(n):
        prop_instance = prop_type()
        rental_list.append(prop_instance)
        print(f'Property Type: {prop_type.__name__} {i} created')
