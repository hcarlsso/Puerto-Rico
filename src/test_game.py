import unittest as ut
from unittest.mock import MagicMock
# import unittest.mock as mock
import factory as f
from controller import QuitGame

class TestGame(ut.TestCase):

    def test_play_game(self):

        view = f.get_view('terminal')
        # view = ut.mock.MagicMock()
        controller = ut.mock.MagicMock()

        # view.Setup = ut.mock.MagicMock()
        setup = ut.mock.MagicMock()
        setup.get_player_names = ut.mock.MagicMock(
            return_value = ['a', 'b','c']
        )

        p1 = MagicMock()
        p1.select_index = MagicMock(side_effect = QuitGame())
        p2 = MagicMock()
        p2.select_index = MagicMock(return_value = 0)
        p3 = MagicMock()
        p3.select_index = MagicMock(return_value = 0)

        controller.Player.side_effect = [p1, p2,p3]
        controller.Setup = ut.mock.MagicMock(return_value = setup)

        game = f.create_game(view, controller)

        try:
            game.play()
        except QuitGame:
            pass

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
        setup = ut.mock.Mock()
        setup.get_player_names.return_value = ['a','b','c']

        mock_view = ut.mock.Mock()
        mock_control = ut.mock.Mock()
        players = f.create_players(
            setup,
            mock_view,
            mock_control
        )

        self.assertEqual(len(players),3)


class TestColonist(ut.TestCase):

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


class TestPlantation(ut.TestCase):

    def test(self):

        portal = f.create_tiles_portal(3)
        self.assertDictEqual(
            portal.get_state(),{'on_display': [], 'plantations': 50, 'quarries': 8}
        )
        import random
        random.seed(0)
        portal.fill_display()

        self.assertDictEqual(
            portal.get_state(),
            {'on_display': ['Coffee', 'Corn', 'Corn', 'Indigo'],
             'plantations': 46, 'quarries': 8}
        )

        q = portal.take_quarry()
        self.assertDictEqual(
            portal.get_state(),
            {'on_display': ['Coffee', 'Corn', 'Corn', 'Indigo'],
             'plantations': 46, 'quarries': 7}
        )

        available_tile = portal.get_on_display()
        self.assertDictEqual(
            portal.get_state(),
            {'on_display': [],
             'plantations': 46, 'quarries': 7}
        )

        available_tile.pop()
        portal.return_unselected(available_tile)
        self.assertDictEqual(
            portal.get_state(),
            {'on_display': [],
             'plantations': 49, 'quarries': 7}
        )


    def test_choose_plantaion(self):

        portal = f.create_tiles_portal(3)
        self.assertDictEqual(
            portal.get_state(),{'on_display': [], 'plantations': 50, 'quarries': 8}
        )
        import random
        random.seed(0)
        portal.fill_display()

        self.assertDictEqual(
            portal.get_state(),
            {'on_display': ['Coffee', 'Corn', 'Corn', 'Indigo'],
             'plantations': 46, 'quarries': 8}
        )
        # Choose last option
        player = ut.mock.MagicMock()
        player.choose_plantation = lambda x: x[:-1]

        portal.play_selection(player)
        self.assertDictEqual(
            portal.get_state(),
            {'on_display': ['Coffee', 'Corn', 'Corn'],
             'plantations': 46, 'quarries': 8}
        )

    def test_choose_plantaion_quarry(self):

        portal = f.create_tiles_portal(3)
        self.assertDictEqual(
            portal.get_state(),{'on_display': [], 'plantations': 50, 'quarries': 8}
        )
        import random
        random.seed(0)
        portal.fill_display()

        self.assertDictEqual(
            portal.get_state(),
            {'on_display': ['Coffee', 'Corn', 'Corn', 'Indigo'],
             'plantations': 46, 'quarries': 8}
        )
        # Choose last option
        player = ut.mock.MagicMock()
        player.choose_plantation = lambda x: x[:-1]

        portal.play_selection(player, quarry_option = True)
        self.assertDictEqual(
            portal.get_state(),
            {'on_display': ['Coffee', 'Corn', 'Corn', 'Indigo'],
             'plantations': 46, 'quarries': 7}
        )

if __name__ == '__main__':
    ut.main()
