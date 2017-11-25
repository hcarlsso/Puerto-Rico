class Player:

    def __init__(self):
        pass

    def display_role_options(self, name, roles):
        print('Player {0} choose role:'.format(name))

        for i, role in enumerate(roles):
            print('Index {0}: '.format(i+1) + str(role))
