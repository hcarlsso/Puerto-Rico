from . import Roles as roles
from . import Plantations as plant_types
from . import Buildings as building_types
from . import Goods as good_types
import Utils as ut
import itertools as it

class Setup:

    def __init__(self, view, controller):

        self.view = view
        self.controller = controller

    def get_player_names(self):

        names = self.controller.get_player_names()
        if len(names) > 5:
            raise ValueError('Too many players. Max 5.')

        if len(names) < 3:
            raise ValueError('Too few players. Min 3.')
        return names


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

            self.play_govenor_cycle(next(players_orders))
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
        played_roles = []
        for player_index in order:
            # Choose cards
            # And give
            (chosen, roles_left) = self.players[player_index].choose_role(self.roles)
            # Play card

            # End of round
            self.roles = roles_left
            played_roles.append(chosen)

        # End of Governor cycle
        # Give money to remaining role cards
        for role in self.roles:
            role.add_doublon()

        # Give back cards
        self.roles.extend(played_roles)

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
    def __init__(self, name, view, controller):
        self.doublons = 0
        self.board = None
        self.name = name
        self.view = view
        self.controller = controller

    def recieve_island_tile(self, tile):
        self.board.set_island_tile(tile)

    def is_city_full(self):
        return self.board.is_city_full()

    def choose_role(self, roles):
        # Choose role and give back.
        self.view.display_role_options(self.name, roles)

        index = self.controller.select_role()

        chosen = roles.pop(index)

        return (chosen, roles)



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
