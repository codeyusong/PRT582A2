import unittest


class TestGameLoop(unittest.TestCase):

    def test_game_loop(self):
        # Simulating the user guessing the correct number on the third attempt
        self.attempts = 0
        inputs = iter(['1234', '5678', '9101'])
        self.game_loop(target_number=9101, mock_input_func=inputs.__next__)
        self.assertEqual(self.attempts, 3)

        # Simulating the user quitting before guessing correctly
        self.attempts = 0
        inputs = iter(['1234', 'quit'])
        self.game_loop(target_number=9101, mock_input_func=inputs.__next__)
        self.assertEqual(self.attempts, 2)

    def game_loop(self, target_number, mock_input_func):
        while True:
            self.attempts += 1
            guess = mock_input_func()
            if guess == 'quit' or int(guess) == target_number:
                break


# Running the test
test_suite = unittest.TestLoader().loadTestsFromTestCase(TestGameLoop)
unittest.TextTestRunner().run(test_suite)
