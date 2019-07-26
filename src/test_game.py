from unittest.mock import MagicMock
import unittest as ut
import factory as f
from controller import QuitGame

class TestGame(ut.TestCase):

    def test_get_total_state(self):

        view = f.get_view('terminal')

        setup = ut.mock.MagicMock()
        setup.get_player_names = ut.mock.MagicMock(
            return_value = ['a', 'b','c']
        )

        p1 = MagicMock()
        p2 = MagicMock()
        p3 = MagicMock()

        controller = ut.mock.MagicMock()
        controller.Player.side_effect = [p1, p2,p3]
        controller.Setup = ut.mock.MagicMock(return_value = setup)

        game = f.create_game(view, controller)

        self.maxDiff = None
        # import pprint as pp
        # pp.pprint(game.get_total_state())
        ref = {
            'players': [
                {'name':'a',
                 'doubloons' : 2,
                 'victory_points': 0,
                 'unemployed_colonists': 0,
                 'board': {
                     'city_spaces' : [],
                     'island_spaces' : [('Indigo', {'occupied': False})],
                 }
                },
                {'name':'b',
                 'doubloons' : 2,
                 'victory_points': 0,
                 'unemployed_colonists': 0,
                 'board': {
                     'city_spaces' : [],
                     'island_spaces' : [('Indigo', {'occupied': False})],
                 }
                },
                {
                    'name':'c',
                    'doubloons' : 2,
                    'victory_points': 0,
                    'unemployed_colonists': 0,
                    'board': {
                        'city_spaces' : [],
                        'island_spaces' : [('Corn', {'occupied': False})],
                    }
                }
            ],
            'colonist': {
                'ship': 0, 'supply': 55
            },
            'tiles': {
                'on_display': ['Corn', 'Indigo', 'Indigo', 'Sugar'],
                'plantations': 43,
                'quarries': 8
            },
            'remaining_victory_points': 75,
            'available_goods': {
                'coffee': 9,
                'corn': 10,
                'indigo': 11,
                'sugar': 11,
                'tobacco': 9
            },
            'available_buildings': {
                'City Hall': 1,
                'Coffee Roaster': 2,
                'Construction Hut': 2,
                'Customs House': 1,
                'Factory': 2,
                'Fortress': 1,
                'Guild Hall': 1,
                'Hacienda': 2,
                'Harbor': 2,
                'Hospice': 2,
                'Indigo Plant': 2,
                'Large Market': 2,
                'Large Warehouse': 2,
                'Office': 2,
                'Residence': 1,
                'Small Indigo Plant': 3,
                'Small Market': 2,
                'Small Sugar Mill': 3,
                'Small Warehouse': 2,
                'Sugar Mill': 2,
                'Tobacco Storage': 2,
                'University': 2,
                'Wharf': 2
            }
        }
        out = game.get_total_state()
        tiles_test = out.pop('tiles')
        tiles_ref = ref.pop('tiles')
        self.assertDictEqual(out,ref)

        self.assertEqual(tiles_test['plantations'], tiles_ref['plantations'])
        self.assertEqual(tiles_test['quarries'], tiles_ref['quarries'])

        self.assertEqual(len(tiles_test['on_display']), 4)
        for t in tiles_test['on_display']:
            self.assertIn(t, ['Corn', 'Indigo', 'Indigo', 'Sugar', 'Tobacco', 'Coffee'])


    def test_play_game(self):

        view = f.get_view('terminal')
        controller = ut.mock.MagicMock()

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

        self.assertRaises(QuitGame, game.play)


    def test_create_game_wrong_number_of_players(self):

        view = f.get_view('terminal')
        players = f.create_players_model(
            'asdasd', None, None)
        self.assertRaises(ValueError, f.prepare_game, players, view)

    def test_governor_order(self):

        view = f.get_view('terminal')
        players = f.create_players_model(
            'asd', None, None)
        game = f.prepare_game(players, view)

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
            portal.get_state(),
            {'on_display': [],
             'plantations': 50, 'quarries': 8}
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
            portal.get_state(),
            {'on_display': [], 'plantations': 50, 'quarries': 8}
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
