import property
import random


class Purchase(Property):
    def __init__(self, sqft, num_beds, num_baths, price, mortgage_term=25, interest=0.072):
        super().__init__(sqft, num_beds, num_baths)
        self.price = price  # subclass-specific random generation instead of here
        self.mortgage_term = mortgage_term
        self.interest = interest


class Condo(Purchase):
    def __init__(self):
        sqft = random.randint(350, 800)
        num_beds = 1
        num_baths = 1
        price = random.randint(300000, 500000)
        super().__init__(sqft, num_beds, num_baths, price)

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

    def display_condo(self):
        print(f'The price of this condo is: ${self.price}.00')
        print(f'The mortgage on this condo is ${self.mortgage}.00 per month')
        print(f'The square footage of this condo is: {self.sqft} ft.')
        print(f'This condo has {self.num_beds} bedrooms')
        print(f'This condo has {self.num_baths} bathrooms')
        print(f'Condo interest rate: {self.interest}')


class TownHome(Purchase):
    def __init__(self):
        sqft = random.randint(800, 1800)  # Adjust the range as appropriate
        num_beds = random.randint(2, 4)
        num_baths = random.randint(1, 3)
        price = random.randint(550000, 700000)
        mortgage = random.randint(1000, 7000)
        super().__init__(sqft, num_beds, num_baths, price, mortgage)


class Duplex(Purchase):
    def __init__(self):
        sqft = random.randint(1000, 2000)
        num_beds = random.randint(2, 5)
        num_baths = random.randint(2, 4)
        price = random.randint(250000, 450000)
        mortgage = random.randint(1200, 8000)
        super().__init__(sqft, num_beds, num_baths, price, mortgage)


class Bungalow(Purchase):
    def __init__(self):
        sqft = random.randint(900, 1500)
        num_beds = random.randint(2, 3)
        num_baths = random.randint(1, 2)
        price = random.randint(150000, 350000)
        mortgage = random.randint(900, 5000)
        super().__init__(sqft, num_beds, num_baths, price, mortgage)


class Mansion(Purchase):
    def __init__(self):
        sqft = random.randint(5000, 20000)
        num_beds = random.randint(5, 10)
        num_baths = random.randint(4, 8)
        price = random.randint(1000000, 5000000)
        mortgage = random.randint(5000, 20000)
        super().__init__(sqft, num_beds, num_baths, price, mortgage)


prop_list = []


def gen_props(n, prop_type):
    for i in range(n):
        prop_list.append(prop_type)
        print(f'Property Type: {prop_type} {i} created')
