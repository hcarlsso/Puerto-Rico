import unittest

import factory as f

class TestGame(unittest.TestCase):

    def test_create_game(self):

        game = f.prepare_game(range(3))

        # self.assertEqual('foo'.upper(), 'FOO')

    def test_create_game_wrong_number_of_players(self):

        self.assertRaises(ValueError, f.prepare_game, range(6))

    def test_governor_order(self):

        game = f.prepare_game(range(3))

        order = game.get_player_orders(3)


        # The orders
        self.assertListEqual(next(order), [0,1,2])
        self.assertListEqual(next(order), [1,2,0])
        self.assertListEqual(next(order), [2,0,1])
        self.assertListEqual(next(order), [0,1,2])

    def test_create_players(self):

        players = f.create_players(['a','b','c'])

        self.assertEqual(len(players),3)
if __name__ == '__main__':
    unittest.main()
