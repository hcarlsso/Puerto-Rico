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

    def view_player(self, player, tabs=0):

        prefix_0 = self.prefix * tabs
        print(prefix_0 + "Player: " + player['name'])
        prefix = self.prefix * (tabs + 1)

        print(prefix + 'Doubloons: ' + str(player['doubloons']))
        print(prefix + 'Victory Points: ' + str(player['victory_points']))
        board = player['board']

        print(prefix + 'Buildings:')
        prefix_2 = self.prefix * (tabs + 2)

        for building in board['city_spaces']:
            print(prefix_2 + building)

        print(prefix + 'Tiles:')
        for building in board['island_spaces']:
            print(prefix_2 + building)
