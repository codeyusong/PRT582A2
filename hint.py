import unittest

class TestHintGeneration(unittest.TestCase):

    def test_hint_generation(self):
        # All digits are correct and in the right spot
        self.assertEqual(self.generate_hints('1234', '1234'), 'o o o o')

        # All digits are wrong in value and spot
        self.assertEqual(self.generate_hints('1234', '5678'), '# # # #')

        # Two digits are correct and in the right spot, two are wrong in value and spot
        self.assertEqual(self.generate_hints('1234', '1256'), 'o o # #')

        # Two digits are correct but in the wrong spot, two are wrong in value and spot
        self.assertEqual(self.generate_hints('1234', '5612'), '# # x x')

        # Mixed hints: one digit correct and in right spot, one digit correct but in wrong spot, two digits wrong in value and spot
        self.assertEqual(self.generate_hints('1234', '1245'), 'o o x #')

    def generate_hints(self, target, guess):
        hints = []
        for i, j in zip(target, guess):
            if i == j:
                hints.append('o')
            elif j in target:
                hints.append('x')
            else:
                hints.append('#')
        return ' '.join(hints)


# Running the updated test again
test_suite = unittest.TestLoader().loadTestsFromTestCase(UpdatedTestHintGeneration)
unittest.TextTestRunner().run(test_suite)
