import factory as f

if __name__ == '__main__':
    N_players = input('How many players?:')
    player_names = []

    for i in range(N_players):
        player_names.append(
            input('Player name for player number {:d}:'.format(i+1))
        )


    game = f.prepare_game(N_players)

    n_player_start = input('Who will start? ' + '[1-' + str(N_players) + ')]')
