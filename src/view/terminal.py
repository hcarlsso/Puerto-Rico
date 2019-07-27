# coding: utf-8

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

class Setup:
    '''
    Should contain more
    '''
    def __init__(self):

        pass

class Game:

    def __init__(self):
        self.prefix = "\t"

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
        self.view_buildings(state['available_buildings'])

    def view_player(self, player, tabs=0):

        prefix_0 = self.prefix * tabs
        print(prefix_0 + "Player: " + player['name'])
        prefix = self.prefix * (tabs + 1)

        print(prefix + 'Doubloons: ' + str(player['doubloons']))
        print(prefix + 'Victory Points: ' + str(player['victory_points']))
        print(prefix + 'Unemployed colonists: ' + str(player['unemployed_colonists']))
        board = player['board']

        print(prefix + 'Buildings:')
        prefix_2 = self.prefix * (tabs + 2)

        for (building, state) in board['city_spaces']:
            print(prefix_2 + building)

        print(prefix + 'Tiles:')
        for (building, state) in board['island_spaces']:
            if state == 1:
                string = 'Occupied'
            else:
                string = 'Unoccupied'
            print(prefix_2 + building + self.prefix + string)

    def view_colonist_supply(self, colonist_state, tabs=0):
        """
        Display info concerning colonist supply
        """

        print("Colonist info:")
        prefix_0 = self.prefix * (tabs + 1)
        print(prefix_0 + "Colonist on ship: " + str(colonist_state['ship']))
        print(prefix_0 + "Colonist supply: " + str(colonist_state['supply']))

    def view_plantations(self, state, tabs=0):

        print("Plantation info:")
        prefix_0 = self.prefix * (tabs + 1)
        print(prefix_0 + "Plantations left: " + str(state['plantations']))
        print(prefix_0 + "Quarries left: " + str(state['quarries']))
        print(prefix_0 + "Available plantations: " + str(state['on_display']))


    def view_goods(self, state, tabs=0):
        goods = ['coffee', 'corn', 'indigo', 'sugar', 'tobacco']

        print("Available goods:")
        prefix_0 = self.prefix * (tabs + 1)
        for good in goods:
            print(prefix_0 + good + ": " + str(state[good]))

    def view_buildings(self, state, tabs=0):
        print("Available buildings:")

        mapping = {
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
            'wharf' : 'Wharf'
        }
        prefix_0 = self.prefix * (tabs + 1)

        for key in sorted(mapping.keys()):
            print(prefix_0 + mapping[key] + ": " + str(state[key]))
