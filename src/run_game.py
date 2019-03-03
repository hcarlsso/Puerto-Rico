import factory as f

if __name__ == '__main__':


    view_mod = f.get_view('terminal')
    controller_mod = f.get_controller('terminal')

    game = f.create_game(view_mod, controller_mod)

    game.play()
