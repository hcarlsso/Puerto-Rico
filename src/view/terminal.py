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
