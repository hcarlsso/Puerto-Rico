import factory as f

if __name__ == '__main__':


    gui_option = 'terminal'

    game = f.create_game(gui_option)

    game.play()
