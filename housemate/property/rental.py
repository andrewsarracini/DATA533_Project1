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
        print("")


class RentalCondo(Rental):
    def __init__(self):
        sqft = random.randint(350, 850)
        num_beds = random.randint(1, 2)
        num_baths = 1
        rent = random.randint(1400, 1900)
        utilities = random.randint(100, 150)
        super().__init__(sqft, num_beds, num_baths, rent, utilities)


class RentalTownHome(Rental):
    def __init__(self):
        sqft = random.randint(800, 1800)
        num_beds = random.randint(2, 4)
        num_baths = random.randint(1, 3)
        rent = random.randint(2200, 3200)
        utilities = random.randint(200, 250)
        super().__init__(sqft, num_beds, num_baths, rent, utilities)


class RentalDuplex(Rental):
    def __init__(self):
        sqft = random.randint(1400, 2000)
        num_beds = random.randint(2, 5)
        num_baths = random.randint(2, 4)
        rent = random.randint(2800, 4000)
        utilities = random.randint(250, 300)
        super().__init__(sqft, num_beds, num_baths, rent, utilities)


class RentalBungalow(Rental):
    def __init__(self):
        sqft = random.randint(1300, 2400)
        num_beds = random.randint(4, 5)
        num_baths = random.randint(3, 4)
        rent = random.randint(3400, 4600)
        utilities = random.randint(300, 400)
        super().__init__(sqft, num_beds, num_baths, rent, utilities)


class RentalTwoStory(Rental):
    def __init__(self):
        sqft = random.randint(2000, 3300)
        num_beds = random.randint(4, 6)
        num_baths = random.randint(3, 5)
        rent = random.randint(4500, 6100)
        utilities = random.randint(350, 450)
        super().__init__(sqft, num_beds, num_baths, rent, utilities)


class RentalMansion(Rental):
    def __init__(self):
        sqft = random.randint(8000, 12000)
        num_beds = random.randint(8, 10)
        num_baths = random.randint(7, 8)
        rent = random.randint(10000, 13000)
        utilities = random.randint(500, 675)
        super().__init__(sqft, num_beds, num_baths, rent, utilities)


def gen_rental(n, prop_type):
    rental_list = []
    for i in range(n):
        prop_instance = prop_type()
        rental_list.append(prop_instance)
        # print(f'{prop_type.__name__} {i} generated \n')
    return rental_list


def rental_recommendation(prop_type, income, pref_beds):
    rec_rent_list = []
    generated_rent_list = gen_rental(25, prop_type)
    for i in range(len(generated_rent_list)):
        if (income * 0.6) > generated_rent_list[i].calc_total_rent() and pref_beds <= generated_rent_list[i].num_beds:
            rec_rent_list.append(generated_rent_list[i])

    if rec_rent_list:
        print(
            f' **************\nCongratulations! You have {len(rec_rent_list)} recommendations!\n **************')

    if not rec_rent_list:
        print("You have no recommendations. Consider changing your preferences")
    return rec_rent_list


def view_rental_list(ren_list):
    i = 0
    # Flag to controls when to iterate
    display_next = True

    while i < len(ren_list):
        if display_next:
            ren_list[i].display_rental()

        user_next = input(
            "Type 'next' to see the next rental option or 'stop' to exit: ")
        if user_next == 'next':
            # Iterate and flag set to True
            i += 1
            display_next = True
        elif user_next == 'stop':
            break
        else:
            # Don't iterate and flag set to False
            display_next = False
            print("Invalid input. Please type 'next' to continue or 'stop' to exit. \n")
