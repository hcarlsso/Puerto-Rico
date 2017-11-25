import unittest
import unittest.mock as mock
import factory as f
import tests.mock_view as mv
import tests.mock_controller as mc

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
        setup = mock.Mock()
        setup.get_player_names.return_value = ['a','b','c']

        mock_view = mock.Mock()
        mock_control = mock.Mock()
        players = f.create_players(
            setup,
            mock_view,
            mock_control
        )

        self.assertEqual(len(players),3)


class TestColonist(unittest.TestCase):

    def test(self):
        portal = f.create_colonist_portal(3)

        self.assertDictEqual(
            portal.get_state(), {'ship': 0, 'supply': 55}
        )

        portal.fill_ship(10)

        self.assertDictEqual(
            portal.get_state(), {'ship': 10, 'supply': 45}
        )

        colonists = list(portal.empty_ship())

        self.assertEqual(len(colonists), 10)
        self.assertDictEqual(
            portal.get_state(), {'ship': 0, 'supply': 45}
        )

        portal.fill_ship(55)
        self.assertDictEqual(
            portal.get_state(), {'ship': 45, 'supply': 0}
        )
        self.assertTrue(portal.is_game_over())
        self.assertEqual(len(list(portal.empty_ship())), 45)
        self.assertTrue(portal.is_game_over())

if __name__ == '__main__':
    unittest.main()
