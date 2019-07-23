from . import QuitGame

class Player:

    def __init__(self):
        pass

    def select_index(self):
        '''
        Select a number
        '''
        text = 'Which index?'
        inp = self.display_question(text)
        return int(inp) - 1

    def display_question(self, text):
        '''
        Do the command input
        '''
        text_cmd = text + ' [q to quit/s to show game]: '
        while True:
            resp = input(text_cmd)
            if resp == 'q':
                raise QuitGame
            elif resp == 's':
                pass
            else:
                break
        return resp

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
