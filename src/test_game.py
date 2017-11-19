import unittest

import factory as f

class TestGame(unittest.TestCase):

    def test_create_game(self):

        game = f.prepare_game(3)

        # self.assertEqual('foo'.upper(), 'FOO')

    def test_create_game_wrong_number_of_players(self):

        self.assertRaises(ValueError, f.prepare_game, 6)


if __name__ == '__main__':
    unittest.main()
