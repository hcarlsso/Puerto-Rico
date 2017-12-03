import factory as f

if __name__ == '__main__':


    gui_option = 'terminal'

    view_mod = f.get_view(options)
    controller_mod = f.get_controller(options)

    game = f.create_game(gui_option, view_mod, controller_mod)

    game.play()
