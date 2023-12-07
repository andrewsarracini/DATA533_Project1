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
    # setup() not useful here because each subclass has different attribute ranges

    def setUp(self):
        random.seed(533)

    def test_condo(self):
        condo_inst = Condo()
        self.assertTrue(350 <= condo_inst.sqft <= 800)
        self.assertTrue(1 <= condo_inst.num_beds <= 2)
        self.assertTrue(1 == condo_inst.num_baths)
        self.assertTrue(300000 <= condo_inst.price <= 500000)

    def test_townhome(self):
        townhome_inst = TownHome()
        self.assertTrue(800 <= townhome_inst.sqft <= 1800)
        self.assertTrue(2 <= townhome_inst.num_beds <= 4)
        self.assertTrue(1 <= townhome_inst.num_baths <= 3)
        self.assertTrue(550000 <= townhome_inst.price <= 700000)

    def test_duplex(self):
        duplex_inst = Duplex()
        self.assertTrue(1000 <= duplex_inst.sqft <= 2100)
        self.assertTrue(2 <= duplex_inst.num_beds <= 5)
        self.assertTrue(2 <= duplex_inst.num_baths <= 4)
        self.assertTrue(550000 <= duplex_inst.price <= 850000)

    def test_bungalow(self):
        bungalow_inst = Bungalow()
        self.assertTrue(1100 <= bungalow_inst.sqft <= 2300)
        self.assertTrue(4 <= bungalow_inst.num_beds <= 5)
        self.assertTrue(3 <= bungalow_inst.num_baths <= 4)
        self.assertTrue(700000 <= bungalow_inst.price <= 1000000)

    def test_twostory(self):
        twostory = TwoStory()
        self.assertTrue(1800 <= twostory.sqft <= 3300)
        self.assertTrue(4 <= twostory.num_beds <= 7)
        self.assertTrue(3 <= twostory.num_baths <= 6)
        self.assertTrue(1000000 <= twostory.price <= 2000000)

    def test_mansion(self):
        mansion = Mansion()
        self.assertTrue(5000 <= mansion.sqft <= 12000)
        self.assertTrue(8 <= mansion.num_beds <= 10)
        self.assertTrue(7 <= mansion.num_baths <= 8)
        self.assertTrue(1000000 <= mansion.price <= 5000000)

    def test_calculate_mortgage(self):
        purchase_known = Purchase(1500, 6, 3, 700000)
        purchase2_known = Purchase(25000, 7, 5, 1500000)
        self.assertEqual(purchase_known.calculate_mortgage(0.15), 4281.55)
        self.assertEqual(purchase2_known.calculate_mortgage(0.15), 9174.76)

    def test_display(self):
        purchase_known = Purchase(1500, 4, 3, 700000)

        # Below code specifies that the output is a print statement!
        to_terminal = io.StringIO()
        sys.stdout = to_terminal
        purchase_known.display()
        sys.stdout = sys.__stdout__

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
        self.assertEqual(result[0].price, 2086128)
        self.assertEqual(result[1].sqft, 8377)
        self.assertEqual(result[2].num_beds, 9)

    # This function requires user input-- come back here later!
    # def test_view_purchase_list(self):

    def test_purchase_recommend(self):
        result = purchase_recommendation(TownHome, 150000, 100000, 3)
        self.assertEqual(len(result), 15)
        for instance in result:
            self.assertIsInstance(instance, TownHome)
        self.assertEqual(result[10].price, 676460)
        self.assertEqual(result[7].sqft, 1020)
        self.assertEqual(result[2].num_baths, 1)

    unittest.main(argv=[''], verbosity=2, exit=False)
