# coding: utf-8

MAPPING_BUILDINGS = {
    'city_hall' : 'City Hall',
    'coffee_roaster' : 'Coffee Roaster',
    'construction_hut' : 'Construction Hut',
    'customs_house' : 'Customs House',
    'factory':'Factory',
    'fortress' :'Fortress',
    'guild_hall' : 'Guild Hall',
    'hacienda' : 'Hacienda',
    'harbor' : 'Harbor',
    'hospice' : 'Hospice',
    'indigo_plant' :'Indigo Plant',
    'large_market':'Large Market',
    'large_warehouse' :'Large Warehouse',
    'office' : 'Office',
    'residence' : 'Residence',
    'small_indigo_plant' : 'Small Indigo Plant',
    'small_market' : 'Small Market',
    'small_sugar_mill' : 'Small Sugar Mill',
    'small_warehouse' : 'Small Warehouse',
    'sugar_mill' : 'Sugar Mill',
    'tobacco_storage' : 'Tobacco Storage',
    'university' : 'University',
    'wharf' : 'Wharf',
    'indigo' : 'Indigo',
    'sugar' : 'Sugar',
    'corn' : 'Corn',
    'coffee' : 'Coffee',
    'tobacco' : 'Tobacco',
    'quarry' : 'Quarry'
}
LAYOUT_BUILDINGS = [
    ['small_indigo_plant', 'indigo_plant', 'tobacco_storage','guild_hall'],
    ['small_sugar_mill', 'sugar_mill', 'coffee_roaster', 'residence'],
    ['small_market', 'hospice', 'factory', 'fortress'],
    ['hacienda', 'office', 'university','customs_house'],
    ['construction_hut', 'large_market', 'harbor', 'city_hall'],
    ['small_warehouse','large_warehouse', 'wharf']
]
MAPPING_GOODS = {
    'indigo' : 'Indigo',
    'sugar' : 'Sugar',
    'corn' : 'Corn',
    'coffee' : 'Coffee',
    'tobacco' : 'Tobacco'
}


class Player:

    def __init__(self):
        pass

    def display_options(self, name, roles):
        '''
        Display options in a list
        '''
        print('Player {0} choose role:'.format(name))

        for i, role in enumerate(roles):
            print('Index {0}: '.format(i+1) + str(role))

    def got_doubloon(self, player, doubloons):

        print(
            "Player {:s} got {:d} doubloons. Total count: {:d}".format(
                player.name, doubloons, player.doubloons
            )
        )

    def display_question_colonist_from_supply(self, name):
        print('Does player {0} want colonist from supply?'.format(name))

    def display_reception_colonists(self, name, n_colonists):
        if n_colonists > 1:
            print('Player {0} received {1} colonists'.format(name, n_colonists))
        else:
            print('Player {0} received {1} colonist'.format(name, n_colonists))

    def ask_unload_san_juan(self, name, n_colonists):
        print(
            'Player {0} have {1} colonists in San Juan, place them?'.format(
                name,
                n_colonists
            )
        )
    def ask_unload_any_building(self, name, n_colonists):
        print(
            'Player {0} have {1} colonists on board, unload them?'.format(
                name,
                n_colonists
            )
        )
    def show_spaces(self, name, empty_spaces):
        print(
            'Player {0} choose index:'.format(
                name
            )
        )
        for (i, space) in enumerate(empty_spaces):
            print('Index {0}: '.format(i+1) + str(space))

    def show_buildings(self, name, buildings_w_price):
        print(
            'Player {0} choose index for building:'.format(
                name
            )
        )
        print('Index {0:>2}:{1:>25}'.format(0, 'Buy no building'))
        for (i, (building, price)) in enumerate(buildings_w_price):
            print(
                'Index {0:>2}:{1:>25}{2:>3} doubloons'.format(
                    i+1,
                    MAPPING_BUILDINGS[building],
                    price
                )
            )
    def placed_colonist_on_building(self, name, b_name):
        print(
            'Player {0} placed colonist on {1}'.format(
                name,
                b_name
            )
        )
    def place_colonists_on_san_juan(self, name, n_colonists):
        print(
            'Player {0} placed {1} colonist(s) in San Juan'.format(
                name,
                n_colonists
            )
        )

class Setup:
    '''
    Should contain more
    '''
    def __init__(self):

        pass

class Game:

    def __init__(self):
        self.prefix = "  "

    def view_state(self, state):
        '''
        View state of the total game
        '''
        print("Game state:")
        for player in state['players']:
            self.view_player(player, 0)

        self.view_colonist_supply(state['colonist'])
        self.view_plantations(state['tiles'])

        print("Available victory points: " + str(state['remaining_victory_points']))
        self.view_goods(state['available_goods'])
        self.view_cargo_ships(state['cargo_ships'])
        self.view_buildings(state['available_buildings'])

    def view_cargo_ships(self, state, tabs=0):
        prefix_0 = self.prefix * tabs
        print(prefix_0 + "Cargo ships:")

        prefix_1 = self.prefix * (tabs + 1)
        info_str = ' '.join(
            ['Size {0}: {1} {2}'.format(
                size,
                len(state[size]),
                state[size][0] if state[size] else ' '
            ) for size in sorted(state.keys())]
        )
        print(prefix_1 + info_str)

    def view_player(self, player, tabs=0):

        prefix_0 = self.prefix * tabs
        print(prefix_0 + "Player: " + player['name'])

        prefix = self.prefix * (tabs + 1)
        print(
            prefix + 'Doubloons:{0:>2},\tVictory Points:{1:>2},\tUnemployed colonists:{2:>2}'.format(
                player['doubloons'],
                player['victory_points'],
                player['unemployed_colonists']
            )
        )
        board = player['board']

        # Buildings
        print(
            prefix + 'Buildings {0}/{1}:'.format(
                board['space_occupancy_city'],
                board['space_occupancy_city_max']
            )
        )
        prefix_2 = self.prefix * (tabs + 2)

        for (building, state) in board['city_spaces']:

            print(
                prefix_2 + '{0:>17}, {1}/{2}'.format(
                    MAPPING_BUILDINGS[str(building)],
                    state['occupancy'],
                    state['capacity']
                )
            )

        # Plantations
        print(
            prefix + 'Plantations {0}/{1}:'.format(
                board['space_occupancy_plantation'],
                board['space_occupancy_plantation_max']
            )
        )
        for (building, state) in board['island_spaces']:
            print(
                prefix_2 + '{0:>8}, {1}/{2}'.format(
                    MAPPING_BUILDINGS[str(building)],
                    state['occupancy'],
                    state['capacity']
                )
            )
        # Goods
        print(prefix + 'Goods:')
        good_str = ' '.join(
            ['{0}: {1}, '.format(MAPPING_GOODS[str(good)], good_count)
             for (good, good_count) in player['goods'].items()]
        )
        print(prefix_2 + good_str)

    def view_colonist_supply(self, colonist_state, tabs=0):
        """
        Display info concerning colonist supply
        """

        print("Colonist info:")
        prefix_0 = self.prefix * (tabs + 1)
        print(
            prefix_0 + "Colonist on ship: {0}, Colonist supply: {1}".format(
                colonist_state['ship'],
                colonist_state['supply']
            )
        )

    def view_plantations(self, state, tabs=0):

        print("Plantation info:")
        prefix_0 = self.prefix * (tabs + 1)
        print(
            prefix_0 + "Plantations left:{0:>8}, Quarries left:{1:>8},".format(
                state['plantations'],
                state['quarries'],
                state['on_display']
            )
        )

        print(prefix_0 + "Available plantations: "  + ' '.join(
                ["{0:>4}".format(MAPPING_BUILDINGS[p]) for p in state['on_display']]
            )
        )


    def view_goods(self, state, tabs=0):
        goods = ['coffee', 'corn', 'indigo', 'sugar', 'tobacco']

        print("Available goods:")
        prefix_0 = self.prefix * (tabs + 1)
        good_str = ' '.join(
            ['{0}: {1},'.format(MAPPING_GOODS[str(good)], state[good])
             for good in goods]
        )
        print(prefix_0 + good_str)

    def view_buildings(self, state, tabs=0):
        print("Available buildings:")


        prefix_0 = self.prefix * (tabs + 1)

        for row_items in LAYOUT_BUILDINGS:
            print(
                prefix_0 + ''.join(['{0:>18}: {1}'.format(
                    MAPPING_BUILDINGS[key],
                    state[key]
                ) for key in row_items])
            )
