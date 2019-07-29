'''
Main classes in model.
'''
import itertools as it
from collections import Counter

import Utils as ut

from . import Roles as role_types
from . import Plantations as plant_types
from . import Buildings as building_types
from . import Goods as good_types



class Setup:
    '''
    Setup
    '''
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
    '''
    Root object of game
    '''
    def __init__(self, players, roles, cargo_ships, colonist_portal,
                 tiles_portal, victory_points, buildings, goods, trading_house,
                 view):

        self.players = players
        self.roles = roles
        self.current_role = None

        # The state of the game
        self.cargo_ships = cargo_ships
        self.colonist_portal = colonist_portal
        self.tiles_portal = tiles_portal
        self.victory_points = victory_points
        self.available_buildings = buildings
        self.available_goods = goods
        self.trading_house = trading_house

        self.view = view

        # Always first player have index
        self.govenor_index = 0

    def get_total_state(self):

        state = {}

        state['players'] = [p.get_state() for p in self.players]
        state['colonist'] = self.colonist_portal.get_state()
        state['tiles'] = self.tiles_portal.get_state()
        state['remaining_victory_points'] = len(self.victory_points)
        state['available_goods'] = {
            str(k) : len(v) for (k,v) in self.available_goods.items()
        }
        state['available_buildings'] = dict(
            Counter([str(p) for p in self.available_buildings])
        )
        state['trading_house'] = self.trading_house.get_state()
        state['roles_doubloon_count'] = [
            (str(r), r.doubloons) for r in self.roles
        ]
        state['current_role'] = str(self.current_role) if self.current_role is not None else None
        state['cargo_ships'] = {
            cap: ship.get_state() for (cap, ship) in self.cargo_ships.items()
        }
        return state

    def get_player_orders(self, n_players):

        # player_order
        a = list(range(n_players))

        return it.cycle([a[i:] + a[:i] for i in range(len(a))])

    def play(self):
        '''
        Main loop of game
        '''
        # Prepare other stuff
        players_orders = self.get_player_orders(len(self.players))

        game_over = False

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

        n_players = len(self.players)
        for i in  range(start_index, start_index+n_players):

            if i >= n_players:
                index = i - n_players
            else:
                index = i

            yield self.players[index]

    def play_govenor_cycle(self, order):
        '''
        The Governor begins the round by choosing a role.
        Then the other players can choose a role
        '''

        played_roles = []
        for player_index in order:

            self.view.view_state(self.get_total_state())
            # Choose cards
            # And give
            (chosen, roles_left) = self.players[player_index].choose_role(
                self.roles,
                self
            )

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
        '''
        Play a single role card.
        '''
        if role.need_all_players():
            role.play_with_all_players(order_player, self)
        else:
            for i, player in enumerate(order_player):

                # First player get privilege
                if i == 0:
                    role.play(player, self, privilege=True)
                else:
                    role.play(player, self)

class Player:
    '''
    Class what each player controls
    '''
    def __init__(self, name, view, controller):
        self.doubloons = 0
        self.board = None
        self.name = name
        self.victory_points = []
        self.unemployed_colonists = [] # Also known as San Juan
        self.goods = []
        self.is_governor = False
        self.have_played_role = False

        self.view = view
        self.controller = controller

    def add_goods(self, goods):
        self.goods.extend(goods)

    def get_state(self):

        return dict(
            name=self.name,
            doubloons=self.doubloons,
            board=self.board.get_state(),
            victory_points=len(self.victory_points),
            unemployed_colonists=len(self.unemployed_colonists),
            is_governor=self.is_governor,
            have_played_role=self.have_played_role,
            goods=dict(
                Counter([str(g) for g in self.goods])
            )
        )

    def recieve_island_tile(self, tile):
        self.board.set_island_tile(tile)

    def is_city_full(self):
        return self.board.is_city_full()

    def choose_role(self, roles_to_select, game):
        '''
        Choose role and give back.
        '''
        self.view.display_options(self.name, roles_to_select)
        index = self.controller.select_index()
        chosen = roles_to_select.pop(index)
        return (chosen, roles_to_select)

    def recieve_doubloons(self, doubloons):
        self.doubloons += doubloons
        self.view.got_doubloon(self, doubloons)

    def choose_plantation(self, options):

        self.view.display_options(self.name, options)
        index = self.controller.select_index()
        chosen = options.pop(index)
        self.board.set_island_tile(chosen)

        # Return remaining
        return options

    def recieve_colonists(self, colonists):
        '''
        Receive a list of colonists.

        Implement code for how to place them
        '''
        self.view.display_reception_colonists(self.name, len(colonists))
        # Check if colonists in San Juan should be place
        if self.unemployed_colonists:
            self.view.ask_unload_san_juan(
                self.name,
                len(self.unemployed_colonists)
            )
            number_of_colonists_from_san_juan = self.controller.get_a_number(
                0,
                len(self.unemployed_colonists)
            )
            if number_of_colonists_from_san_juan > 0:
                colonists.extend(
                    [self.unemployed_colonists.pop()
                     for i in range(number_of_colonists_from_san_juan)]
                )

        # Check if any spaces should be unloaded
        n_colonists_board = self.board.get_number_of_colonists()
        if n_colonists_board > 0:
            self.view.ask_unload_any_building(
                self.name,
                n_colonists_board
            )
            resp = self.controller.get_a_number(0, n_colonists_board)
            if resp == n_colonists_board:
                #unload all
                occupied_spaces = self.board.get_occupied_spaces()
                colonists.extend(
                    [s.take_colonist()  for s in occupied_spaces]
                )
            elif resp > 0:
                occupied_spaces = self.board.get_occupied_spaces()
                for i in range(resp):
                    self.view.show_spaces(self.name, occupied_spaces)
                    index = self.controller.select_index()
                    space_to_unload = occupied_spaces.pop(index)
                    colonists.append(
                        space_to_unload.take_colonist()
                    )
            # If zero do nothing

        # Place the colonists, must place if possible
        empty_spaces = self.board.get_empty_spaces()
        for i in range(len(empty_spaces)):
            self.view.show_spaces(self.name, empty_spaces)
            index = self.controller.select_index()
            building_to_load = empty_spaces.pop(index)
            colonist_to_load = colonists.pop()

            building_to_load.add_colonist(colonist_to_load)

        # The excess to San Juan
        self.unemployed_colonists.extend(colonists)
    def get_empty_city_spaces(self):
        '''
        Return number of empty city spaces
        '''
        return 0
    def wants_colonist_from_supply(self):
        '''
        Display and ask questions
        '''
        self.view.display_question_colonist_from_supply(self.name)
        return self.controller.get_true_or_false()


class Board:
    '''
    The board each player has.
    '''

    def __init__(self):
        self.island_spaces = []
        self.city_spaces = []
        self.max_space = 12

    def get_state(self):

        return dict(
            island_spaces=[
                (str(p), p.get_state())
                for p in self.island_spaces
            ],
            city_spaces=[
                (str(p), p.get_state())
                for p in self.city_spaces
            ]
        )
    def get_occupied_spaces(self):
        occupied_spaces = []
        for p in self.island_spaces:
            if p.get_number_of_colonists() > 0:
                occupied_spaces.append(p)

        for b in self.city_spaces:
            capacity = b.get_number_of_colonists()
            for i in range(capacity):
                occupied_spaces.append(b)

        return occupied_spaces
    def get_empty_spaces(self):
        '''
        Empty spaces including multiple on a single production building
        '''
        empty_spaces = []
        for p in self.island_spaces:
            if p.get_number_of_colonists() == 0:
                empty_spaces.append(p)

        for b in self.city_spaces:
            capacity = b.colonist_capacity - b.get_number_of_colonists()
            for i in range(capacity):
                empty_spaces.append(b)

        return empty_spaces
    def get_number_of_unoccupied_spaces(self):
        number = 0
        for p in self.island_spaces:
            if p.get_number_of_colonists() == 0:
                number += 1

        for b in self.city_spaces:
            number += b.colonist_capacity - b.get_number_of_colonists()

        return number
    def get_occupied_buildings(self):
        return [
            (str(p), p.get_number_of_colonists()) for p in self.island_spaces if
            p.get_number_of_colonists() > 1
        ] + [
            (str(p), p.get_number_of_colonists()) for p in self.city_spaces if
            p.get_number_of_colonists() > 1
        ]
    def get_number_of_colonists(self):
        return  sum([
            p.get_number_of_colonists() for p in self.island_spaces
        ]) + sum([
            p.get_number_of_colonists() for p in self.city_spaces
        ])

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
    def __init__(self, n_cargo_max):
        self.cargo = []
        self.n_cargo_max = n_cargo_max

    def available_capacity(self):
        return self.n_cargo_max - len(self.cargo)

    def is_ship_full(self):
        return len(self.cargo) == self.n_cargo_max

    def load(self, goods):
        self.cargo.extend(goods)
        if len(self.cargo) > self.n_cargo_max:
            raise ValueError('Too Much')
    def flush_ship(self):
        self.cargo = []
    def get_state(self):
        return [str(good) for good in self.cargo]

class TradingHouse:
    def __init__(self):
        self.spaces = []

    def add_good(self, good):
        if len(self.spaces) < 4:
            self.spaces.append(good)
        else:
            raise ValueError('House is full')
    def flush(self):
        temp = self.spaces
        self.spaces = []
        return temp
    def is_full(self):
        return len(self.spaces) == 4
    def get_state(self):
        return [str(g) for g in self.spaces]
