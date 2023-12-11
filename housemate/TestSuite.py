# TestSuite.py

import sys
import unittest

from user.TestUserLogin import TestUserProfileLoading, TestViewProfile, TestEditProfile, TestDeleteProfile
from user.TestUserProfile import TestUserProfile, TestAppendToDataFrame, TestSaveDataFrameToCSV
from user.TestSecurity import TestStringHash, TestReverseHash, TestCheckCredentials
from test_purchase import TestPurchase
from test_rental import TestRental

# sys.path
# sys.path.append('c:\\Users\\cadla\\OneDrive\\Desktop\\DATA533\\Project\\DATA533_Project1\\housemate')

if __name__ == '__main__':
    # Create a test suite
    test_suite = unittest.TestSuite()
    result = unittest.TestResult()
    test_suite.addTest(unittest.makeSuite(TestUserProfile))
    test_suite.addTest(unittest.makeSuite(TestAppendToDataFrame))
    test_suite.addTest(unittest.makeSuite(TestSaveDataFrameToCSV))

    # Create a test runner
    test_runner = unittest.TextTestRunner()

    # Run the tests WRAPPED PRINT
    print(test_runner.run(test_suite))
    
# my_suite()

