import model.Roles as roles
import model.Plantations as plant_types
import model.Buildings as building_types
import model.Goods as good_types
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


def create_role_cards(N_players):

    standard_cards = [
        roles.Captain(),
        roles.Trader(),
        roles.Settler(),
        roles.Builder(),
        roles.Mayor(),
        roles.Craftsman(),
    ]
    if N_players > 3:
        # 4 and 5 players
        standard_cards.append(roles.Prospector())
    if N_players > 4:
        # 5 players
        standard_cards.append(roles.Prospector())
    if N_players > 5:
        raise ValueError('Wrong number of players.')

    return standard_cards

def create_players(setup, view_mod, controller_mod):
    '''
    player_names: list of strings
    '''

    player_names = setup.get_player_names()
    N_players = len(player_names)
    players = []

    N_start_doublons = N_players - 1
    for i in range(N_players):
        p = mod.Player(player_names[i],
                   view_mod.Player(),
                   controller_mod.Player())

        p.doublons = N_start_doublons

        # Add board empty board
        p.board = mod.Board()
        players.append(p)

    return players

def create_cargo_ships(N_players):

    # Define cargo ships
    if N_players == 3:
        N_cargo_ships = [4,5,6]
    elif N_players == 4:
        N_cargo_ships = [5,6, 7]
    elif N_players == 5:
        N_cargo_ships = [6,7,8]
    else:
        raise

    return [mod.CargoShip(i) for i in N_cargo_ships]

def create_victory_points(N_players):

    if N_players == 3:
        N_start_VP = 75
    elif N_players == 4:
        N_start_VP = 100
    elif N_players == 5:
        N_start_VP = 122
    else:
        raise

    return [mod.VictoryPoint() for i in range(N_start_VP)]

def create_colonists(N_players):

    if N_players == 3:
        # Define number of colonist
        N_colonists = 55
    elif N_players == 4:
        # Define number of colonist
        N_colonists = 75
    elif N_players == 5:
        # Define number of colonist
        N_colonists = 95
    else:
        raise
    return [mod.Colonist() for i in range(N_colonists)]


def create_island_tiles():

    island_tiles = []

    island_tiles.extend(
        [plant_types.Quarry() for i in range(8)]
    )

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

def prepare_game(players):


    g = mod.Game()

    g.players = players
    N_players = len(players)

    g.N_plantation_tiles_show = N_players + 1
    g.roles = create_role_cards(N_players)
    g.cargo_ships = create_cargo_ships(N_players)
    g.victory_points = create_victory_points(N_players)
    g.colonist_supply = create_colonists(N_players)

    # Non player dependent
    g.available_island_tiles = create_island_tiles()
    g.available_buildings = create_buildings()
    g.available_goods = create_goods()

    return g

def get_setup(view_mod, controller_mod):


    setup = mod.Setup(
        view = view_mod.Setup(),
        controller = controller_mod.Setup()
    )
    return setup


def create_game(options):


    view_mod = get_view(options)
    controller_mod = get_controller(options)

    setup = get_setup(view_mod,controller_mod)

    players = create_players(setup, view_mod, controller_mod)

    game = prepare_game(players)

    return game
