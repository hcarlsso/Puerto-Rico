import factory as f

if __name__ == '__main__':
    N_players = int(input('How many players?:'))
    player_names = []

    print('In the order of starting.')
    for i in range(N_players):
        player_names.append(
            input('Player name for player number {:d}:'.format(i+1))
        )

    players = f.create_players(player_names)

    game = f.prepare_game(players)

    game.play()
    # n_player_start = int(input('Who will start? ' + '[1-' + str(N_players) + ']:'))
