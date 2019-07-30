from . import QuitGame

class Player:

    def __init__(self):
        pass

    def select_index(self, end, start=0):
        '''
        Select a number
        '''
        text = 'Which index?'
        while True:
            inp = self.display_question(text)
            if int(inp)-1 in range(start, end):
                return int(inp) - 1

    def get_true_or_false(self):
        text = 'y/n?'
        while True:
            resp = self.display_question(text)
            if resp == 'y':
                return True
            if resp == 'n':
                return False
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
                # not implemented yet
                pass
            else:
                break
        return resp
    def get_a_number(self, n_start, n_end):
        text = 'How many? [{0}-{1}]'.format(n_start, n_end)
        while True:
            inp = self.display_question(text)
            if inp in range(n_start, n_end + 1):
                break
        return int(inp)

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
