import unittest
import random


class TestNumberGeneration(unittest.TestCase):

    def test_four_digit_number(self):
        number = self.generate_number()
        self.assertTrue(1000 <= number <= 9999)  # Check the number value

    def generate_number(self):
        return random.randint(1000, 9999)


# Running the test
test_suite = unittest.TestLoader().loadTestsFromTestCase(TestNumberGeneration)
unittest.TextTestRunner().run(test_suite)
