from property import Property
import random


class Purchase(Property):
    def __init__(self, sqft, num_beds, num_baths, price, mortgage_term=25, interest=0.072):
        super().__init__(sqft, num_beds, num_baths)
        self.price = price  # subclass-specific random generation instead of here
        self.mortgage_term = mortgage_term
        self.interest = interest

    def calculate_mortgage(self, downpay=0.10):
        # 10% Downpayment is a PLACEHOLDER for the variable amount
        # Waiting for Profile.downpayment to input into this method
        down_payment = self.price * downpay
        principal = self.price - down_payment
        monthly_interest_rate = self.interest / 12
        total_payments = self.mortgage_term * 12

        # Mortgage calc using compound interest
        monthly_mortgage = principal * (monthly_interest_rate * (1 + monthly_interest_rate)
                                        ** total_payments) / ((1 + monthly_interest_rate) ** total_payments - 1)
        return round(monthly_mortgage, 2)

    def display(self):
        class_name = type(self).__name__
        print(f'Purchase type: {class_name}')
        monthly_mortgage = self.calculate_mortgage()
        print(f'Price: ${self.price}')
        print(f'Monthly mortgage: ${monthly_mortgage}')
        print(f'Square footage: {self.sqft}sqft.')
        print(f'Number of bedrooms: {self.num_beds}')
        print(f'Number of bathrooms: {self.num_baths}')


class Condo(Purchase):
    def __init__(self):
        sqft = random.randint(350, 800)
        num_beds = random.randint(1, 2)
        num_baths = 1
        price = random.randint(300000, 500000)
        super().__init__(sqft, num_beds, num_baths, price)


class TownHome(Purchase):
    def __init__(self):
        sqft = random.randint(800, 1800)
        num_beds = random.randint(2, 4)
        num_baths = random.randint(1, 3)
        price = random.randint(550000, 700000)
        super().__init__(sqft, num_beds, num_baths, price)


class Duplex(Purchase):
    def __init__(self):
        sqft = random.randint(1000, 2100)
        num_beds = random.randint(2, 5)
        num_baths = random.randint(2, 4)
        price = random.randint(550000, 850000)
        super().__init__(sqft, num_beds, num_baths, price)


class Bungalow(Purchase):
    def __init__(self):
        sqft = random.randint(1100, 2300)
        num_beds = random.randint(4, 5)
        num_baths = random.randint(3, 4)
        price = random.randint(700000, 1000000)
        super().__init__(sqft, num_beds, num_baths, price)


class TwoStory(Purchase):
    def __init__(self):
        sqft = random.randint(1800, 3300)
        num_beds = random.randint(4, 7)
        num_baths = random.randint(3, 6)
        price = random.randint(1000000, 2000000)
        super().__init__(sqft, num_beds, num_baths, price)


class Mansion(Purchase):
    def __init__(self):
        sqft = random.randint(5000, 12000)
        num_beds = random.randint(8, 10)
        num_baths = random.randint(7, 8)
        price = random.randint(1000000, 5000000)
        super().__init__(sqft, num_beds, num_baths, price)


prop_list = []


def gen_props(n, prop_type):
    for i in range(n):
        prop_instance = prop_type()
        prop_list.append(prop_instance)
        print(f'Property Type: {prop_type.__name__} {i} created')
