import unittest
import sys
import io
import random

from property.property import Property
from property.purchase import (
    Purchase,
    Condo,
    TownHome,
    Duplex,
    Bungalow,
    TwoStory,
    Mansion,
    gen_purchase,
    view_purchase_list,
    purchase_recommendation
)


class TestPurchase(unittest.TestCase):
    @ classmethod
    def classSetUp(cls):
        # Placeholder here as it's stated as a requirement
        print('Set Up Class')

    def setUp(self):
        random.seed(533)
        self.condo_inst = Condo()
        self.townhome_inst = TownHome()
        self.duplex_inst = Duplex()
        self.bungalow_inst = Bungalow()
        self.twostory = TwoStory()
        self.mansion = Mansion()
        self.purchase_known = Purchase(1500, 6, 3, 700000)
        self.purchase2_known = Purchase(25000, 7, 5, 1500000)
        self.purchase3_known = Purchase(1500, 4, 3, 700000)

    def test_condo(self):
        self.assertTrue(350 <= self.condo_inst.sqft <= 800)
        self.assertTrue(1 <= self.condo_inst.num_beds <= 2)
        self.assertTrue(1 == self.condo_inst.num_baths)
        self.assertTrue(300000 <= self.condo_inst.price <= 500000)

    def test_townhome(self):
        self.assertTrue(800 <= self.townhome_inst.sqft <= 1800)
        self.assertTrue(2 <= self.townhome_inst.num_beds <= 4)
        self.assertTrue(1 <= self.townhome_inst.num_baths <= 3)
        self.assertTrue(550000 <= self.townhome_inst.price <= 700000)

    def test_duplex(self):
        self.assertTrue(1000 <= self.duplex_inst.sqft <= 2100)
        self.assertTrue(2 <= self.duplex_inst.num_beds <= 5)
        self.assertTrue(2 <= self.duplex_inst.num_baths <= 4)
        self.assertTrue(550000 <= self.duplex_inst.price <= 850000)

    def test_bungalow(self):
        self.assertTrue(1100 <= self.bungalow_inst.sqft <= 2300)
        self.assertTrue(4 <= self.bungalow_inst.num_beds <= 5)
        self.assertTrue(3 <= self.bungalow_inst.num_baths <= 4)
        self.assertTrue(700000 <= self.bungalow_inst.price <= 1000000)

    def test_twostory(self):
        self.assertTrue(1800 <= self.twostory.sqft <= 3300)
        self.assertTrue(4 <= self.twostory.num_beds <= 7)
        self.assertTrue(3 <= self.twostory.num_baths <= 6)
        self.assertTrue(1000000 <= self.twostory.price <= 2000000)

    def test_mansion(self):
        self.assertTrue(5000 <= self.mansion.sqft <= 12000)
        self.assertTrue(8 <= self.mansion.num_beds <= 10)
        self.assertTrue(7 <= self.mansion.num_baths <= 8)
        self.assertTrue(1000000 <= self.mansion.price <= 5000000)

    def test_calculate_mortgage(self):
        self.assertEqual(self.purchase_known.calculate_mortgage(0.15), 4281.55)
        self.assertEqual(
            self.purchase2_known.calculate_mortgage(0.15), 9174.76)

    def test_display(self):
        # Below code specifies that the output is a print statement!
        to_terminal = io.StringIO()
        sys.stdout = to_terminal
        self.purchase3_known.display()

        expected_print = (
            "Purchase type: Purchase\n"
            "Price: $700000\n"
            "Monthly mortgage: $4281.55\n"
            "Square footage: 1500sqft.\n"
            "Number of bedrooms: 4\n"
            "Number of bathrooms: 3"
        )
        self.assertEqual(to_terminal.getvalue().strip(), expected_print)

    def test_gen_purchase(self):
        result = gen_purchase(3, Mansion)
        self.assertEqual(len(result), 3)
        for instance in result:
            self.assertIsInstance(instance, Mansion)
        self.assertEqual(result[0].price, 1003413)
        self.assertEqual(result[1].sqft, 6108)
        self.assertEqual(result[2].num_beds, 10)

    # This function requires user input-- come back here later!
    # def test_view_purchase_list(self):

    def test_purchase_recommend(self):
        result = purchase_recommendation(TownHome, 150000, 100000, 3)
        self.assertEqual(len(result), 18)
        for instance in result:
            self.assertIsInstance(instance, TownHome)
        self.assertEqual(result[10].price, 581738)
        self.assertEqual(result[7].sqft, 1155)
        self.assertEqual(result[2].num_baths, 1)

    def tearDown(self):
        sys.stdout = sys.__stdout__

    @classmethod
    def tearDownClass(cls):
        # tearDownClass is a requirement
        print('Tear Down Class')


unittest.main(argv=[''], verbosity=2, exit=False)
