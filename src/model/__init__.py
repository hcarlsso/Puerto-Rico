from . import Roles as roles
from . import Plantations as plant_types
from . import Buildings as building_types
from . import Goods as good_types
import Utils as ut
import itertools as it
from collections import Counter

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
        self.roles = None

        # The state of the game
        self.cargo_ships = None
        self.colonist_portal = None
        self.tiles_portal = None

        self.victory_points = None

        self.available_buildings = None
        self.available_goods = None

        # Always first player have index
        self.govenor_index = 0

    def get_total_state(self):

        state = {}

        state['players'] = [p.get_state() for p in self.players]
        state['colonist'] = self.colonist_portal.get_state()
        state['tiles'] = self.tiles_portal.get_state()
        state['remaining_victory_points'] = len(self.victory_points)
        state['available_goods'] = dict(
            Counter([str(p) for p in self.available_goods])
        )
        return state

    def get_player_orders(self, N_players):

        # player_order
        a = list(range(N_players))

        return it.cycle([a[i:] + a[:i] for i in range(len(a))])

    def play(self):
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
            self.colonist_portal.is_game_over(),
            not self.victory_points # No more victory points
        ]

        conditions.extend(
            [p.is_city_full() for p in self.players ]
        )

        return any(conditions)

    def get_player_order(self, start_index):

        N_players = len(self.players)
        for i in  range(start_index, start_index+N_players):

            if i >= N_players:
                index = i - N_players
            else:
                index = i

            yield self.players[index]

    def play_govenor_cycle(self, order):
        # The Governor begins the round by choosing a role.
        # Then the other players can choose a role
        played_roles = []
        for player_index in order:
            # Choose cards
            # And give
            (chosen, roles_left) = self.players[player_index].choose_role(self.roles)

            # Play card
            order_players = self.get_player_order(player_index)
            self.play_role(chosen, order_players)

            # End of round
            self.roles = roles_left
            played_roles.append(chosen)

        # End of Governor cycle
        # Give money to remaining role cards
        for role in self.roles:
            role.add_doublon()

        # Give back cards
        self.roles.extend(played_roles)

    def play_role(self, role, order_player):

        for i, player in enumerate(order_player):

            # First player get privilege
            if i == 0:
                role.play_privilege(player, self)
            else:
                role.play_ordinary(player, self)


    def prepare_pre_start(self):

        # Give out money
        N_start_doublons = len(self.players) - 1
        for p in self.players:
            p.doubloons = N_start_doublons

        # Do indigo
        indigo = ut.iterate_and_remove(
            self.tiles_portal.plantations,
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
            self.tiles_portal.plantations,
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


class Player:
    def __init__(self, name, view, controller):
        self.doubloons = 0
        self.board = None
        self.name = name
        self.victory_points = []

        self.view = view
        self.controller = controller

    def get_state(self):

        return dict(
            name = self.name,
            doubloons = self.doubloons,
            board = self.board.get_state(),
            victory_points = len(self.victory_points)
        )

    def recieve_island_tile(self, tile):
        self.board.set_island_tile(tile)

    def is_city_full(self):
        return self.board.is_city_full()

    def choose_role(self, roles):
        # Choose role and give back.
        self.view.display_options(self.name, roles)
        index = self.controller.select_index()
        chosen = roles.pop(index)
        return (chosen, roles)

    def recieve_doublons(self, doublons):
        self.doublons += doublons
        self.view.got_doublon(self, doublons)

    def choose_plantation(self, options):

        self.view.display_options(self.name, roles)
        index = self.controller.select_index()
        chosen = options.pop(index)
        self.board.set_island_tile(chosen)

        # Return remaining
        return options

class Board:

    def __init__(self):
        self.island_spaces = []
        self.city_spaces = []
        self.max_space = 12

    def get_state(self):

        return dict(
            island_spaces = [str(p) for p in self.island_spaces],
            city_spaces = [str(p) for p in self.city_spaces]
        )

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
