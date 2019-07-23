import model.Roles as roles
import model.Plantations as plant_types
import model.Buildings as building_types
import model.Goods as good_types
import model.Colonist as col
import model as mod
import Utils as ut
import itertools as it

def get_controller(option):

    if option == 'terminal':
        from controller import terminal as mod
    else:
        pass

    return mod

def get_view(option):

    if option == 'terminal':
        from view import terminal as viewoption
    else:
        pass

    return viewoption


def create_role_cards(n_players):

    standard_cards = [
        roles.Captain(),
        roles.Trader(),
        roles.Settler(),
        roles.Builder(),
        roles.Mayor(),
        roles.Craftsman(),
    ]
    if n_players > 3:
        # 4 and 5 players
        standard_cards.append(roles.Prospector())
    if n_players > 4:
        # 5 players
        standard_cards.append(roles.Prospector())
    if n_players > 5:
        raise ValueError('Wrong number of players.')

    return standard_cards

def create_players(setup, view_mod, controller_mod):
    '''
    player_names: list of strings
    '''

    player_names = setup.get_player_names()
    players = []


    for i in range(len(player_names)):
        p = mod.Player(player_names[i],
                   view_mod.Player(),
                   controller_mod.Player())

        # Add board empty board
        p.board = mod.Board()
        players.append(p)

    return players

def create_cargo_ships(n_players):

    # Define cargo ships
    if n_players == 3:
        n_cargo_ships = [4, 5, 6]
    elif n_players == 4:
        n_cargo_ships = [5, 6, 7]
    elif n_players == 5:
        n_cargo_ships = [6, 7, 8]
    else:
        raise

    return [mod.CargoShip(i) for i in n_cargo_ships]

def create_victory_points(n_players):

    if n_players == 3:
        n_start_vp = 75
    elif n_players == 4:
        n_start_vp = 100
    elif n_players == 5:
        n_start_vp = 122
    else:
        raise

    return [mod.VictoryPoint() for i in range(n_start_vp)]

def create_colonists(n_players):

    if n_players == 3:
        # Define number of colonist
        n_colonists = 55
    elif n_players == 4:
        # Define number of colonist
        n_colonists = 75
    elif n_players == 5:
        # Define number of colonist
        n_colonists = 95
    else:
        raise
    return [col.Colonist() for i in range(n_colonists)]

def create_colonist_portal(n_players):

    supply = create_colonists(n_players)
    ship = col.Ship()

    portal = col.Portal(ship, supply)

    return portal

def create_plantation_tiles():

    island_tiles = []


    island_tiles.extend(
        [plant_types.Coffee() for i in range(8)]
    )

    island_tiles.extend(
        [plant_types.Tobacco() for i in range(9)]
    )

    island_tiles.extend(
        [plant_types.Corn() for i in range(10)]
    )

    island_tiles.extend(
        [plant_types.Sugar() for i in range(11)]
    )

    island_tiles.extend(
        [plant_types.Indigo() for i in range(12)]
    )

    return island_tiles

def create_tiles_portal(n_players):

    quarries = [plant_types.Quarry() for i in range(8)]
    tiles = create_plantation_tiles()

    return plant_types.Portal(n_players + 1, quarries, tiles)

def create_buildings():

    buildings = []

    buildings.extend(
        [building_types.IndigoPlant() for i in range(2)]
    )

    buildings.extend(
        [building_types.SmallMarket() for i in range(2)]
    )

    return buildings

def create_goods():

    goods = []

    goods.extend(
        [good_types.Coffee() for i in range(9)]
    )

    goods.extend(
        [good_types.Tobacco() for i in range(9)]
    )

    goods.extend(
        [good_types.Corn() for i in range(10)]
    )
    goods.extend(
        [good_types.Sugar() for i in range(11)]
    )

    goods.extend(
        [good_types.Indigo() for i in range(11)]
    )

    return goods

def prepare_game(players, view_mod):
    '''
    Create the overall game object
    '''

    n_players = len(players)
    game = mod.Game(
        players,
        create_role_cards(n_players),
        create_cargo_ships(n_players),
        create_colonist_portal(n_players),
        create_tiles_portal(n_players),
        create_victory_points(n_players),
        create_buildings(),
        create_goods(),
        view_mod.Game()
    )


    game.N_plantation_tiles_show = n_players + 1

    return game

def get_setup(view_mod, controller_mod):


    setup = mod.Setup(
        view=view_mod.Setup(),
        controller=controller_mod.Setup()
    )
    return setup


def create_game(view_mod, controller_mod):


    setup = get_setup(view_mod, controller_mod)
    players = create_players(setup, view_mod, controller_mod)
    game = prepare_game(players, view_mod)

    return game
