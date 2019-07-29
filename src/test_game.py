from unittest.mock import MagicMock
import unittest as ut
import factory as f
import Utils as utils
from controller import QuitGame

class TestGame(ut.TestCase):

    def test_load_game_from_state(self):

        state_input = {
            'players': [ # this is the order of playing roles
                {
                    'name':'a',
                    'doubloons' : 2,
                    'victory_points': 1,
                    'is_governor' : True,
                    'have_played_role': False,
                    'unemployed_colonists': 0,
                    'board': {
                        'city_spaces' : [
                            ('indigo_plant', 0)
                        ],
                        'island_spaces' : [
                            ('indigo', 0)
                        ],
                    },
                    'goods': {
                        'coffee': 1,
                        'corn': 1,
                        'indigo': 1,
                        'sugar': 1,
                        'tobacco': 1,
                    },
                },
                {
                    'name':'b',
                    'is_governor' : False,
                    'have_played_role': False,
                    'doubloons' : 2,
                    'victory_points': 0,
                    'unemployed_colonists': 0,
                    'board': {
                        'city_spaces' : [],
                        'island_spaces' : [
                            ('indigo', 0)
                        ],
                    },
                    'goods': {},
                },
                {
                    'name':'c',
                    'doubloons' : 2,
                    'is_governor' : False,
                    'have_played_role': False,
                    'victory_points': 0,
                    'unemployed_colonists': 0,
                    'board': {
                        'city_spaces' : [],
                        'island_spaces' : [
                            ('corn', 0)
                        ],
                    },
                    'goods': {},
                }
            ],
            'current_role' : 'trader',
            'roles_doubloon_count' : [ # to account for multiple prospectors
                ('settler', 1),
                ('captain', 0),
                ('mayor', 0),
                ('craftsman', 1)
            ],
            'trading_house': ['corn'],
            'colonist': {
                'ship': 3,
                'supply': 52
            },
            'tiles': {
                'on_display': ['corn', 'indigo', 'indigo', 'sugar'],
            },
            'cargo_ships' : {
                4 : [],
                5 : ['corn'],
                6 : ['indigo', 'indigo']
            }
        }

        controller = ut.mock.MagicMock()
        view = ut.mock.MagicMock()

        game = f.load_game_from_state(state_input, view, controller)

        state_out = game.get_total_state()

        # The input that is induced
        state_extended = {
            'available_goods': {
                'coffee': 8,
                'corn': 7,
                'indigo': 8,
                'sugar': 10,
                'tobacco': 8
            },
            'available_buildings': {
                'city_hall': 1,
                'coffee_roaster': 3,
                'construction_hut': 2,
                'customs_house': 1,
                'factory': 2,
                'fortress': 1,
                'guild_hall': 1,
                'hacienda': 2,
                'harbor': 2,
                'hospice': 2,
                'indigo_plant': 1,
                'large_market': 2,
                'large_warehouse': 2,
                'office': 2,
                'residence': 1,
                'small_indigo_plant': 3,
                'small_market': 2,
                'small_sugar_mill': 3,
                'small_warehouse': 2,
                'sugar_mill': 2,
                'tobacco_storage': 3,
                'university': 2,
                'wharf': 2
            },
            'tiles': {
                'plantations': 43,
                'quarries': 8
            },
            'remaining_victory_points': 74
        }


        state_ref = utils.deep_dict_merge(state_input, state_extended)

        self.maxDiff = None
        # import pdb; pdb.set_trace()
        self.assertDictEqual(state_out, state_ref)

        # for k in state_out:
        #     self.assertDictEqual(state_out[k], state_ref[k])

    def test_get_total_state(self):

        view = f.get_view('terminal')

        setup = ut.mock.MagicMock()
        setup.get_player_names = ut.mock.MagicMock(
            return_value=['a', 'b', 'c']
        )

        p1 = MagicMock()
        p2 = MagicMock()
        p3 = MagicMock()

        controller = ut.mock.MagicMock()
        controller.Player.side_effect = [p1, p2, p3]
        controller.Setup = ut.mock.MagicMock(return_value=setup)

        game = f.create_game(view, controller)

        self.maxDiff = None
        ref = {
            'players': [
                {'name':'a',
                 'doubloons' : 2,
                 'victory_points': 0,
                 'is_governor' : False,
                 'have_played_role': False,
                 'unemployed_colonists': 0,
                 'board': {
                     'city_spaces' : [],
                     'island_spaces' : [('indigo', {'capacity': 1, 'occupancy': 0})],
                     'space_occupancy_city': 0,
                     'space_occupancy_city_max': 12,
                     'space_occupancy_plantation': 1,
                     'space_occupancy_plantation_max': 12,
                 },
                 'goods' : {
                     'corn': 0,
                     'indigo': 0,
                     'sugar': 0,
                     'tobacco': 0,
                     'coffee' : 0
                 },
                },
                {'name':'b',
                 'doubloons' : 2,
                 'victory_points': 0,
                 'is_governor' : False,
                 'have_played_role': False,
                 'unemployed_colonists': 0,
                 'board': {
                     'city_spaces' : [],
                     'island_spaces' : [('indigo', {'capacity': 1, 'occupancy': 0})],
                     'space_occupancy_city': 0,
                     'space_occupancy_city_max': 12,
                     'space_occupancy_plantation': 1,
                     'space_occupancy_plantation_max': 12,
                 },
                 'goods' : {
                     'corn': 0,
                     'indigo': 0,
                     'sugar': 0,
                     'tobacco': 0,
                     'coffee' : 0
                 },
                },
                {
                    'name':'c',
                    'doubloons' : 2,
                    'victory_points': 0,
                    'is_governor' : False,
                    'have_played_role': False,
                    'unemployed_colonists': 0,
                    'board': {
                        'city_spaces' : [],
                        'island_spaces' : [('corn', {'capacity': 1, 'occupancy': 0})],
                        'space_occupancy_city': 0,
                        'space_occupancy_city_max': 12,
                        'space_occupancy_plantation': 1,
                        'space_occupancy_plantation_max': 12,
                    },
                    'goods' : {
                        'corn': 0,
                        'indigo': 0,
                        'sugar': 0,
                        'tobacco': 0,
                        'coffee' : 0
                 },
                }
            ],
            'colonist': {
                'ship': 3,
                'supply': 52
            },
            'tiles': {
                'on_display': ['corn', 'indigo', 'indigo', 'sugar'],
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
                'city_hall': 1,
                'coffee_roaster': 3,
                'construction_hut': 2,
                'customs_house': 1,
                'factory': 2,
                'fortress': 1,
                'guild_hall': 1,
                'hacienda': 2,
                'harbor': 2,
                'hospice': 2,
                'indigo_plant': 2,
                'large_market': 2,
                'large_warehouse': 2,
                'office': 2,
                'residence': 1,
                'small_indigo_plant': 3,
                'small_market': 2,
                'small_sugar_mill': 3,
                'small_warehouse': 2,
                'sugar_mill': 2,
                'tobacco_storage': 3,
                'university': 2,
                'wharf': 2
            },
            'trading_house': [],
            'roles_doubloon_count': [('captain', 0),
                                     ('trader', 0),
                                     ('settler', 0),
                                     ('builder', 0),
                                     ('mayor', 0),
                                     ('craftsman', 0)],
            'current_role' : None,
            'cargo_ships' : {4:[], 5:[], 6:[]}

        }
        out = game.get_total_state()
        tiles_test = out.pop('tiles')
        tiles_ref = ref.pop('tiles')
        # import pdb; pdb.set_trace()
        self.assertDictEqual(out, ref)

        self.assertEqual(tiles_test['plantations'], tiles_ref['plantations'])
        self.assertEqual(tiles_test['quarries'], tiles_ref['quarries'])

        self.assertEqual(len(tiles_test['on_display']), 4)
        for t in tiles_test['on_display']:
            self.assertIn(t, ['corn', 'indigo', 'indigo', 'sugar', 'tobacco', 'coffee'])


    def test_play_game(self):

        view = f.get_view('terminal')
        controller = ut.mock.MagicMock()

        setup = ut.mock.MagicMock()
        setup.get_player_names = ut.mock.MagicMock(
            return_value=['a', 'b', 'c']
        )

        p_1 = MagicMock()
        p_1.select_index = MagicMock(side_effect=QuitGame())
        p_2 = MagicMock()
        p_2.select_index = MagicMock(return_value=0)
        p_3 = MagicMock()
        p_3.select_index = MagicMock(return_value=0)

        controller.Player.side_effect = [p_1, p_2, p_3]
        controller.Setup = ut.mock.MagicMock(return_value=setup)

        game = f.create_game(view, controller)

        self.assertRaises(QuitGame, game.play)


    def test_create_game_wrong_number_of_players(self):

        self.assertRaises(ValueError, f.create_players_model, 'asdasd', None,None)

    def test_governor_order(self):

        view = f.get_view('terminal')
        players = f.create_players_model(
            'asd', None, None)
        game = f.prepare_game_start(players, view)

        order = game.get_player_orders(3)

        # The orders
        self.assertListEqual(next(order), [0, 1, 2])
        self.assertListEqual(next(order), [1, 2, 0])
        self.assertListEqual(next(order), [2, 0, 1])
        self.assertListEqual(next(order), [0, 1, 2])

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
        portal = f.create_colonist_portal_pre_start(3)

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

    def test_unload_ship(self):

        portal = f.create_colonist_portal_pre_start(3)
        portal.fill_ship(7)

        colonists = portal.get_colonists_from_ship()


        self.assertEqual(len(colonists[0]), 3)
        self.assertEqual(len(colonists[1]), 2)
        self.assertEqual(len(colonists[2]), 2)

        # Ensure it is empty
        state = portal.get_state()
        self.assertEqual(state['ship'], 0)
class TestPlantation(ut.TestCase):

    def test(self):

        portal = f.create_tiles_portal_from_start(3)
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
            {'on_display': ['coffee', 'corn', 'corn', 'indigo'],
             'plantations': 46, 'quarries': 8}
        )

        q = portal.take_quarry()
        self.assertDictEqual(
            portal.get_state(),
            {'on_display': ['coffee', 'corn', 'corn', 'indigo'],
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


    def test_choose_plantation(self):

        portal = f.create_tiles_portal_from_start(3)
        self.assertDictEqual(
            portal.get_state(),{'on_display': [], 'plantations': 50, 'quarries': 8}
        )
        import random
        random.seed(0)
        portal.fill_display()

        self.assertDictEqual(
            portal.get_state(),
            {'on_display': ['coffee', 'corn', 'corn', 'indigo'],
             'plantations': 46, 'quarries': 8}
        )
        # Choose last option
        player = ut.mock.MagicMock()
        player.choose_plantation = lambda x: x[:-1]

        portal.play_selection(player)
        self.assertDictEqual(
            portal.get_state(),
            {'on_display': ['coffee', 'corn', 'corn'],
             'plantations': 46, 'quarries': 8}
        )

    def test_choose_plantation_quarry(self):

        portal = f.create_tiles_portal_from_start(3)
        self.assertDictEqual(
            portal.get_state(),
            {'on_display': [], 'plantations': 50, 'quarries': 8}
        )
        import random
        random.seed(0)
        portal.fill_display()

        self.assertDictEqual(
            portal.get_state(),
            {'on_display': ['coffee', 'corn', 'corn', 'indigo'],
             'plantations': 46, 'quarries': 8}
        )
        # Choose last option
        player = ut.mock.MagicMock()
        player.choose_plantation = lambda x: x[:-1]

        portal.play_selection(player, quarry_option=True)
        self.assertDictEqual(
            portal.get_state(),
            {'on_display': ['coffee', 'corn', 'corn', 'indigo'],
             'plantations': 46, 'quarries': 7}
        )

if __name__ == '__main__':
    ut.main()
