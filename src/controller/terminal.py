class Player:

    def __init__(self):
        pass

    def select_role(self):

        return int(input('Which index? ')) - 1

class Setup:

    def __init__(self):
        pass
    def get_player_names(self):

        N_players = int(input('How many players?:'))

        player_names = []

        print('In the order of starting.')
        for i in range(N_players):
            player_names.append(
                input('Player name for player number {:d}:'.format(i+1))
            )


        return player_names
