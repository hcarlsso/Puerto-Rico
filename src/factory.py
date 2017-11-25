import Roles as roles
import Plantations as plant_types
import Buildings as building_types
import Goods as good_types
import Utils as ut
import itertools as it


class Game:

    def __init__(self):

        self.players = None
        self.cargo_ships = None
        self.roles = None

        self.colonist_supply = None
        self.N_plantation_tiles_show = None
        self.victory_points = None
        self.available_island_tiles = None
        self.available_buildings = None
        self.available_goods = None

        # Always first player have index
        self.govenor_index = 0



    def get_player_orders(self, N_players):

        # player_order
        a = list(range(N_players))

        return it.cycle([a[i:] + a[:i] for i in range(len(a))])

    def play(self):

        # Round number
        i = 1
        # Give tiles
        self.prepare_pre_start()
        # Prepare other stuff
        players_orders = self.get_player_orders(len(self.players))

        game_over  = False

        # Governor cycle
        while not game_over:

            self.play_govenor_cycle(players_orders.next())
            game_over = self.is_game_over()

        print('Game is over')

    def is_game_over(self):


        conditions = [
            not self.colonist_supply, # No more colonist
            not self.victory_points # No more victory points
        ]

        conditions.extend(
            [p.is_city_full() for p in self.players ]
        )

        return any(conditions)

    def play_govenor_cycle(self, order):
        # The Governor begins the round by choosing a role.
        # Then the other players can choose a role
        for player_index in order:
            # Choose cards
            # And give
            (rem, chosen) = self.players[player_index].choose_role(self.roles)
            # Play card
            pass

        # End of Governor cycle
        # Give back cards

    def play_role(self, role):

        pass

    def prepare_pre_start(self):

        # Do indigo
        indigo = ut.iterate_and_remove(
            self.available_island_tiles,
            plant_types.Indigo()
        )

        # Take indigo and give to first player
        self.players[0].recieve_island_tile(next(indigo))

        # Take indigo and give to second player
        self.players[1].recieve_island_tile(next(indigo))

        N_players = len(self.players)

        if N_players == 5:
            # Third player gets indigo
            self.players[2].recieve_island_tile(next(indigo))

        # now the available island tiles should be reduced
        # Do corn
        corn = ut.iterate_and_remove(
            self.available_island_tiles,
            plant_types.Corn()
        )

        if N_players == 3:
            self.players[2].recieve_island_tile(next(corn))
        elif N_players == 4:
            self.players[2].recieve_island_tile(next(corn))
            self.players[3].recieve_island_tile(next(corn))
        else:
            # five players
            self.players[3].recieve_island_tile(next(corn))
            self.players[4].recieve_island_tile(next(corn))


class Colonist:
    def __init__(self):
        pass

class Player:
    def __init__(self, name):
        self.doublons = 0
        self.board = None
        self.name = name

    def recieve_island_tile(self, tile):
        self.board.set_tile(tile)

    def is_city_full(self):
        return self.board.is_city_full()

    def choose_role(self, roles):
        # Choose role and give back.
        return (rem, chosen)
        pass


class Board:

    def __init__(self):
        self.island_spaces = []
        self.city_spaces = []
        self.max_space = 12

    def set_island_tile(self, tile):
        # Each tile has space 1
        if len(self.island_spaces) <= 12:
            self.island_spaces.append(tile)
        else:
            raise

    def set_city_tile(self, tile):
        # Default 12 space
        available_space = self.get_available_space()

        if tile.space <= available_space:
            self.city_spaces.append(tile)
        else:
            raise

    def get_available_space(self):
        return self.max_space - sum([t.space for t in self.city_spaces])

    def is_city_full(self):
        # Assume never below zero
        return self.get_available_space() == 0

class VictoryPoint:

    def __init__(self):
        pass


class CargoShip:
    def __init__(self, N_spaces):

        self.spaces = [None]*N_spaces


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

def create_players(player_names):
    '''
    player_names: list of strings
    '''

    N_players = len(player_names)
    players = []

    N_start_doublons = N_players - 1
    for i in range(N_players):
        p = Player(player_names(i))
        p.doublons = N_start_doublons

        # Add board empty board
        p.board = Board()
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

    return [CargoShip(i) for i in N_cargo_ships]

def create_victory_points(N_players):

    if N_players == 3:
        N_start_VP = 75
    elif N_players == 4:
        N_start_VP = 100
    elif N_players == 5:
        N_start_VP = 122
    else:
        raise

    return [VictoryPoint() for i in range(N_start_VP)]

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
    return [Colonist() for i in range(N_colonists)]


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

    if len(players) > 5:
        raise ValueError('Wrong number of players.')

    g = Game()

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
