import model.Roles as roles
import model.Plantations as plant_types
import model.Buildings as bt
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

    if len(player_names) > 5 or len(player_names) < 3:
        raise ValueError('Wrong number of players.')

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

def create_tile(tile):
    options = {
        'indigo' : plant_types.Indigo,
        'corn' : plant_types.Corn,
        'coffee' : plant_types.Coffee,
        'sugar' : plant_types.Sugar,
        'tobacco' : plant_types.Tobacco,
        'quarry' : plant_types.Quarry
    }
    return options[tile]()

def create_building(name):
    options = {
        'city_hall': bt.CityHall,
        'coffee_roaster' : bt.CoffeeRoaster,
        'construction_hut' : bt.ConstructionHut,
        'customs_house' : bt.CustomsHouse,
        'factory' : bt.Factory,
        'fortress' : bt.Fortress,
        'guild_hall' : bt.GuildHall,
        'hacienda' : bt.Hacienda,
        'harbor' : bt.Harbor,
        'hospice' : bt.Hospice,
        'indigo_plant' : bt.IndigoPlant,
        'large_market' : bt.LargeMarket,
        'large_warehouse' : bt.LargeWarehouse,
        'office' : bt.Office,
        'residence' : bt.Residence,
        'small_indigo_plant' : bt.SmallIndigoPlant,
        'small_market' : bt.SmallMarket,
        'small_sugar_mill' : bt.SmallSugarMill,
        'small_warehouse' : bt.SmallWarehouse,
        'sugar_mill' : bt.SugarMill,
        'tobacco_storage' : bt.TobaccoStorage,
        'university' : bt.University,
        'wharf' : bt.Wharf
    }

    return options[name]()

def create_good(name):
    options = {
        'coffee' : good_types.Coffee,
        'tobacco' : good_types.Tobacco,
        'corn' : good_types.Corn,
        'sugar' : good_types.Sugar,
        'indigo' : good_types.Indigo,
    }
    return options[name]()

def create_role(name):

    options = {
        'captain' : roles.Captain,
        'trader' : roles.Trader,
        'settler' : roles.Settler,
        'builder' : roles.Builder,
        'mayor' : roles.Mayor,
        'craftsman' : roles.Craftsman,
        'prospector' : roles.Prospector,
    }
    return options[name]()



def create_cargo_ships(n_players):

    # Define cargo ships
    if n_players == 3:
        n_cargo_ships = [4, 5, 6]
    elif n_players == 4:
        n_cargo_ships = [5, 6, 7]
    elif n_players == 5:
        n_cargo_ships = [6, 7, 8]
    else:
        raise ValueError('Wrong number of players.')

    return dict([(i, mod.CargoShip(i)) for i in n_cargo_ships])

def create_victory_points(n_players):

    if n_players == 3:
        n_start_vp = 75
    elif n_players == 4:
        n_start_vp = 100
    elif n_players == 5:
        n_start_vp = 122
    else:
        raise ValueError('Wrong number of players.')

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
        raise ValueError('Wrong number of players.')

    return [col.Colonist() for i in range(n_colonists)]

def get_number_of_role_cards(n_players):

    standard_cards = {
        'captain' : 1,
        'trader' : 1,
        'settler' : 1,
        'builder' : 1,
        'mayor' : 1,
        'craftsman' : 1,
    }

    if n_players == 3:
        pass
    elif n_players == 4:
        standard_cards['prospector'] = 1
    elif n_players == 5:
        standard_cards['prospector'] = 2
    else:
        raise ValueError('Wrong number of players.')

    return standard_cards

def get_number_of_plantation_tiles():
    island_tiles = {
        'coffee' :  8,
        'tobacco' : 9,
        'corn' : 10,
        'sugar' : 11,
        'indigo' : 12,
        'quarry' : 8,
    }
    return island_tiles

def get_number_of_goods():
    goods = {
        'coffee' : 9,
        'tobacco' : 9,
        'corn' : 10,
        'sugar' : 11,
        'indigo' : 11,
    }
    return goods

def get_number_of_buildings():

    buildings = {
        'small_indigo_plant' : 3,
        'small_sugar_mill' : 3,
        'small_market' : 2,
        'hacienda' : 2,
        'construction_hut' : 2,
        'small_warehouse' : 2,
        'indigo_plant' : 2,
        'sugar_mill' : 2,
        'hospice' : 2,
        'office' : 2,
        'large_market' : 2,
        'large_warehouse' : 2,
        'tobacco_storage' : 3,
        'coffee_roaster' : 3,
        'factory' : 2,
        'university' : 2,
        'harbor' : 2,
        'wharf' : 2,
        'city_hall': 1,
        'customs_house' : 1,
        'fortress' : 1,
        'guild_hall' : 1,
        'residence' : 1,
    }
    return buildings

def create_all_objects_of_type(count, create_func):
    '''
    Generator objects
    '''
    all_objs = {}
    for (t, c)  in count.items():
        all_objs[t] = [create_func(t) for i in range(c)]

    all_objs_gen = {
        k: (y for y in all_objs[k]) for k in all_objs
    }
    return all_objs_gen

def create_colonist_portal_pre_start(n_players):

    colonists = (y for y in create_colonists(n_players))
    return create_colonist_portal(0, colonists, n_players)

def create_colonist_portal(n_ship, colonists, n_players):

    ship = col.Ship()
    ship.fill_colonists(
        [next(colonists) for i in range(n_ship)]
    )
    supply = list(colonists)
    portal = col.Portal(ship, supply, n_players)

    return portal

def create_tiles_portal_from_start(n_players):


    all_tiles = create_all_objects_of_type(
        get_number_of_plantation_tiles(),
        create_tile
    )
    return create_tiles_portal(all_tiles, n_players)

def create_tiles_portal(tiles, n_players, on_display=[]):
    '''
    Create the object to handle the plantations. Number of tiles that is shown
    is number of players plus one.
    '''

    quarries = list(tiles.pop('quarry'))
    remaining_tiles = list(it.chain.from_iterable(tiles.values()))
    portal = plant_types.Portal(n_players + 1, quarries, remaining_tiles)
    portal.on_display = on_display

    return portal

def prepare_game_start(players, view_mod):
    '''
    Create the overall game object
    '''

    n_players = len(players)

    all_tiles = create_all_objects_of_type(
        get_number_of_plantation_tiles(),
        create_tile
    )

    all_buildings = create_all_objects_of_type(
        get_number_of_buildings(),
        create_building
    )

    all_goods = create_all_objects_of_type(
        get_number_of_goods(),
        create_good
    )
    all_colonists = (y for y in create_colonists(n_players))
    all_vp = (y for y in create_victory_points(n_players))
    all_roles = create_all_objects_of_type(
        get_number_of_role_cards(n_players),
        create_role
    )

    start_doubloons = n_players - 1
    # Give out money
    for player in players:
        player.doubloons = start_doubloons

    # Take indigo and give to first and second player
    players[0].recieve_island_tile(next(all_tiles['indigo']))
    players[1].recieve_island_tile(next(all_tiles['indigo']))
    if n_players == 5:
        # Third player gets indigo
        players[2].recieve_island_tile(next(all_tiles['indigo']))

    if n_players == 3:
        players[2].recieve_island_tile(next(all_tiles['corn']))
    elif n_players == 4:
        players[2].recieve_island_tile(next(all_tiles['corn']))
        players[3].recieve_island_tile(next(all_tiles['corn']))
    else:
        # five players
        players[3].recieve_island_tile(next(all_tiles['corn']))
        players[4].recieve_island_tile(next(all_tiles['corn']))

    # Fill up tiles portal
    tiles_portal = create_tiles_portal(all_tiles, n_players)
    tiles_portal.fill_display()


    colonist_portal = create_colonist_portal(
        n_players,
        all_colonists,
        n_players
    )

    cargo_ships = create_cargo_ships(n_players)
    remaining_buildings = list(it.chain.from_iterable(all_buildings.values()))
    remaining_goods = {
        k : list(v) for (k, v) in all_goods.items()
    }
    remaining_roles = list(it.chain.from_iterable(all_roles.values()))

    trading_house = mod.TradingHouse()

    game = mod.Game(
        players,
        remaining_roles,
        cargo_ships,
        colonist_portal,
        tiles_portal,
        list(all_vp),
        remaining_buildings,
        remaining_goods,
        trading_house,
        view_mod.Game()
    )

    return game


def create_player(name, view, controller):
    player_obj = mod.Player(
        name,
        view.Player(),
        controller.Player(),
    )
    return player_obj

def create_board(state, tiles, buildings, colonists):

    board = mod.Board()
    for (tile_type, occupancy) in state['island_spaces']:
        tile_to_add = next(tiles[tile_type])
        if occupancy == 1:
            tile_to_add.occupy(next(colonists))
        board.set_island_tile(tile_to_add)

    for (building_type, count) in state['city_spaces']:
        building_to_add = next(buildings[building_type])
        building_to_add.add_colonists(
            [next(colonists) for i in range(count)]
        )
        board.set_city_tile(building_to_add)
    return board

def add_player_properties(player, state, tiles, buildings, goods, colonists, vp):


    player.board = create_board(state['board'], tiles, buildings, colonists)
    player.doubloons = state['doubloons']
    player.victory_points = [
        next(vp) for i in range(state['victory_points'])
    ]
    player.is_governor = state['is_governor']
    player.have_played_role = state['have_played_role']
    player.unemployed_colonists = [
        next(colonists) for i in range(state['unemployed_colonists'])
    ]
    for (good_type, count) in state['goods'].items():
        player.add_goods(
            [next(goods[good_type]) for i in range(count)]
        )
    return player

def load_game_from_state(state, view, controller):
    '''
    Load the game from a state.
    '''
    n_players = len(state['players'])

    all_tiles = create_all_objects_of_type(
        get_number_of_plantation_tiles(),
        create_tile
    )

    all_buildings = create_all_objects_of_type(
        get_number_of_buildings(),
        create_building
    )

    all_goods = create_all_objects_of_type(
        get_number_of_goods(),
        create_good
    )
    all_colonists = (y for y in create_colonists(n_players))
    all_vp = (y for y in create_victory_points(n_players))
    all_roles = create_all_objects_of_type(
        get_number_of_role_cards(n_players),
        create_role
    )

    players = []
    for player in state['players']:
        player_obj = mod.Player(
            player['name'],
            view.Player(),
            controller.Player(),
        )
        add_player_properties(
            player_obj, player,
            all_tiles, all_buildings, all_goods, all_colonists, all_vp
        )

        players.append(player_obj)

    if state['current_role'] is not None:
        current_role = next(all_roles[state['current_role']])
    else:
        current_role = None

    remaining_roles = []
    for (role, doubloon_count) in state['roles_doubloon_count']:
        role_i = next(all_roles[role])
        role_i.doubloons = doubloon_count
        remaining_roles.append(role_i)

    trading_house = mod.TradingHouse()
    for good in state['trading_house']:
        trading_house.add_good(next(all_goods[good]))

    colonist_portal = create_colonist_portal(
        state['colonist']['ship'],
        all_colonists,
        n_players
    )

    on_display = [
        next(all_tiles[tile_type]) for tile_type in state['tiles']['on_display']
    ]
    tiles_portal = create_tiles_portal(all_tiles, n_players, on_display)

    # Assume that correct number of cargo ships are included
    cargo_ships = create_cargo_ships(n_players)
    for (cap, ship) in cargo_ships.items():
        ship.load([next(all_goods[load]) for load in state['cargo_ships'][cap]])


    remaining_buildings = list(it.chain.from_iterable(all_buildings.values()))
    remaining_goods = {
        k : list(v) for (k, v) in all_goods.items()
    }


    game = mod.Game(
        players,
        remaining_roles,
        cargo_ships,
        colonist_portal,
        tiles_portal,
        list(all_vp),
        remaining_buildings,
        remaining_goods,
        trading_house,
        view.Game(),
    )

    game.current_role = current_role
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
    game = prepare_game_start(players, view_mod)

    return game
