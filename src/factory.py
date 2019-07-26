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

    return create_players_model(
        player_names,
        view_mod.Player(),
        controller_mod.Player()
    )

def create_players_model(player_names, view, controller):

    players = []

    for p_name in player_names:
        p = mod.Player(
            p_name,
            view,
            controller
        )

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

    island_tiles = [plant_types.Coffee() for i in range(8)] \
        + [plant_types.Tobacco() for i in range(9)] \
        + [plant_types.Corn() for i in range(10)] \
        + [plant_types.Sugar() for i in range(11)] \
        + [plant_types.Indigo() for i in range(12)]

    return island_tiles

def create_tiles_portal(n_players):
    '''
    Create the object to handle the plantations. Number of tiles that is shown
    is number of players plus one.
    '''
    quarries = [plant_types.Quarry() for i in range(8)]
    tiles = create_plantation_tiles()

    return plant_types.Portal(n_players + 1, quarries, tiles)

def create_buildings():

    buildings = [building_types.SmallIndigoPlant() for i in range(3)] \
    + [building_types.SmallSugarMill() for i in range(3)] \
    + [building_types.SmallMarket() for i in range(2)] \
    + [building_types.Hacienda() for i in range(2)] \
    + [building_types.ConstructionHut() for i in range(2)] \
    + [building_types.SmallWarehouse() for i in range(2)] \
    + [building_types.IndigoPlant() for i in range(2)] \
    + [building_types.SugarMill() for i in range(2)] \
    + [building_types.Hospice() for i in range(2)] \
    + [building_types.Office() for i in range(2)] \
    + [building_types.LargeMarket() for i in range(2)] \
    + [building_types.LargeWarehouse() for i in range(2)] \
    + [building_types.TobaccoStorage() for i in range(2)] \
    + [building_types.CoffeeRoaster() for i in range(2)] \
    + [building_types.Factory() for i in range(2)] \
    + [building_types.University() for i in range(2)] \
    + [building_types.Harbor() for i in range(2)] \
    + [building_types.Wharf() for i in range(2)] \
    + [building_types.GuildHall() for i in range(1)] \
    + [building_types.Residence() for i in range(1)] \
    + [building_types.Fortress() for i in range(1)] \
    + [building_types.CustomsHouse() for i in range(1)] \
    + [building_types.CityHall() for i in range(1)]

    return buildings

def create_goods():

    goods = [good_types.Coffee() for i in range(9)] \
        + [good_types.Tobacco() for i in range(9)] \
        + [good_types.Corn() for i in range(10)] \
        + [good_types.Sugar() for i in range(11)] \
        + [good_types.Indigo() for i in range(11)]

    return goods

def prepare_game(players, view_mod):
    '''
    Create the overall game object
    '''

    n_players = len(players)

    # Give out money
    for player in players:
        player.doubloons = n_players - 1

    tiles_portal = create_tiles_portal(n_players)
    # Do indigo
    indigo = ut.iterate_and_remove(
        tiles_portal.plantations,
        plant_types.Indigo()
    )

    # Take indigo and give to first player
    players[0].recieve_island_tile(next(indigo))

    # Take indigo and give to second player
    players[1].recieve_island_tile(next(indigo))

    if n_players == 5:
        # Third player gets indigo
        players[2].recieve_island_tile(next(indigo))

    # now the available island tiles should be reduced
    # Do corn
    corn = ut.iterate_and_remove(
        tiles_portal.plantations,
        plant_types.Corn()
    )

    if n_players == 3:
        players[2].recieve_island_tile(next(corn))
    elif n_players == 4:
        players[2].recieve_island_tile(next(corn))
        players[3].recieve_island_tile(next(corn))
    else:
        # five players
        players[3].recieve_island_tile(next(corn))
        players[4].recieve_island_tile(next(corn))

    # Fill up tiles portal
    tiles_portal.fill_display()

    game = mod.Game(
        players,
        create_role_cards(n_players),
        create_cargo_ships(n_players),
        create_colonist_portal(n_players),
        tiles_portal,
        create_victory_points(n_players),
        create_buildings(),
        create_goods(),
        view_mod.Game()
    )

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
