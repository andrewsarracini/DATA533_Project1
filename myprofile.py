class Profile(object):
    def __init__(self, username: str, password: str, f_name: str, l_name: str, age: int, email: str, downpayment: int, income: int, pref_beds: int):
        self.username = username
        self.password = str(password)
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.email = email
        self.downpayment = int(downpayment)
        self.income = int(income)
        self.pref_beds = int(pref_beds)

    def display_profile(self):
        print(f'Username: {self.username}')
        print(f'Password: {pass_anon(self.password)}')
        print(f'First Name: {self.f_name}')
        print(f'Last Name: {self.l_name}')
        print(f'Age: {self.age}')
        print(f'Email: {self.email}')
        print(f'Downpayment: {self.downpayment}')
        print(f'Annual Income: {self.income}')
        print(f'Desired Number of Bedrooms: {self.pref_beds}')


def pass_anon(password):
    return len(password) * "*"
