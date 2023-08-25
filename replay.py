import unittest


class TestReplayMechanism(unittest.TestCase):

    def test_replay_mechanism(self):
        # Simulating the user deciding to play again and then quitting
        inputs = iter(['play', 'quit'])
        replay_count = self.replay_game(mock_input_func=inputs.__next__)
        self.assertEqual(replay_count, 2)

    def replay_game(self, mock_input_func):
        replay_count = 0
        while True:
            replay_count += 1
            choice = mock_input_func()
            if choice == 'quit':
                break
        return replay_count


# Running the test
test_suite = unittest.TestLoader().loadTestsFromTestCase(TestReplayMechanism)
unittest.TextTestRunner().run(test_suite)
