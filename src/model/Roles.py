from . import definitions

class AbstractRole:
    def __init__(self):
        self.doubloons = 0
    # def __str__(self):
    #     return self.__class__.__name__ + " doubloons: {:d}".format(self.doubloons)

    def add_doublon(self):
        self.doubloons += 1

    def get_stored_doubloons(self, player):
        # Make copy
        player.recieve_doubloons(self.doubloons)

        # Reset
        self.doubloons = 0

    def need_all_players(self):
        return False

class Captain(AbstractRole):
    def need_all_players(self):
        return True

    def perform_shipping(self, player, game, possible_good_kinds,
                         cargo_ship_capacity, player_capacity, extra_vp=0):

        good_type_to_ship = player.choose_good(possible_good_kinds)

        # Figure out loading options
        loading_options = []
        for ship in cargo_ship_capacity:
            if good_type_to_ship in ship['kinds']:
                # The minimum of what player have and what
                # capacity ship have
                loading_options.append(
                    (good_type_to_ship,
                     min(ship['capacity'],
                         player_capacity[good_type_to_ship]),
                     ship['size']
                    )
                            )
        (goods_for_ship, ship_size) = player.choose_good_to_ship(
            loading_options
        )
        n_vps = len(goods_for_ship)
        n_vps += extra_vp
        vps = game.get_victory_points(n_vps)
        player.recieve_victory_points(vps)
        game.load_cargo_ship(ship_size, goods_for_ship)

    def play_with_all_players(self, players, game):

        # Iterate until no one can ship anymore
        j = 0
        while True:
            did_shipping = []
            for (i, player) in enumerate(players):
                if i == 0 and j == 0:
                    super().get_stored_doubloons(player)

                player_capacity = player.get_goods_capacity()
                cargo_ship_capacity = game.get_cargo_ship_capacity()

                player_kinds = set(player_capacity.keys())
                possible_good_kinds = [
                    list(ship['kinds'] & player_kinds)
                    for ship in cargo_ship_capacity
                ]

                # Flatten list and remove duplicate elements
                possible_good_kinds = list({
                    item for sublist in possible_good_kinds for item in sublist
                })

                if possible_good_kinds:
                    if i == 0 and j == 0:
                        # Get only extra victory point for first shipment
                        # and privilege
                        n_vps_extra = 1
                    else:
                        n_vps_extra = 0

                    self.perform_shipping(
                        player, game, possible_good_kinds,
                        cargo_ship_capacity, player_capacity,
                        extra_vp=n_vps_extra
                    )

                    did_shipping.append(True)
                else:
                    did_shipping.append(False)

            if all([action is False for action in did_shipping]):
                break
            j += 1

        # Empty ships
        game.empty_cargo_ships()

        # Empty remaining goods at players
        for player in players:
            goods = player.empty_goods()
            game.recieve_goods(goods)

    def __str__(self):
        return 'captain'

class Trader(AbstractRole):
    def need_all_players(self):
        return True
    def play_with_all_players(self, players, game):
        '''
        Privilege is to get one extra doubloon if sold
        '''
        for (i, player) in enumerate(players):
            if i == 0:
                super().get_stored_doubloons(player)

            trading_capacity = player.get_trading_capacity()
            trading_house_capacity = game.trading_house.get_capacity()

            conditions = [trading_capacity.isdisjoint(trading_house_capacity)]
            conditions.append(not game.trading_house.is_full())

            # No shared elements
            if all(conditions):
                options = list(trading_capacity - trading_house_capacity)
                good = player.choose_good_to_trade(options)
                if good:
                    doubloons = game.trading_house.get_doubloons(good)
                    game.trading_house.add_good(good)

                    # The privilege
                    if i == 0:
                        doubloons += 1
                    player.recieve_doubloons(doubloons)

        # If house full, move goods to supply
        if game.trading_house.is_full():
            goods = game.trading_house.flush()
            for good in goods:
                game.available_goods[str(good)].append(good)

    def __str__(self):
        return 'trader'

class Prospector(AbstractRole):
    def play(self, player, game, privilege=False):
        if privilege:
            super().get_stored_doubloons(player)
            # Recieve 1 doubloon
            player.recieve_doubloons(1)

        # Nothing happens here by default
    def __str__(self):
        return 'prospector'

class Settler(AbstractRole):
    def need_all_players(self):
        return True
    def play_with_all_players(self, players, game):
        for (i, player) in enumerate(players):
            if i == 0:
                super().get_stored_doubloons(player)
                quarry_option = True
            else:
                quarry_option = False

            game.tiles_portal.play_selection(
                player,
                quarry_option=quarry_option
            )

        # Refill
        game.tiles_portal.fill_display()

    def __str__(self):
        return 'settler'

class Builder(AbstractRole):
    def play(self, player, game, privilege=False):
        price_reduction = 0
        if privilege:
            # Get reduction in price
            super().get_stored_doubloons(player)
            price_reduction += 1

        # Filter the buildings that can be bought
        buildings = game.available_buildings
        n_player_quarries = player.get_number_of_active_quarries()
        n_doubloons = player.get_doubloons()

        buildings_with_space = [
            b for b in buildings if
            b.space <= player.get_available_city_space()
        ]

        buildings_with_reduction = []
        for b in buildings_with_space:
            price = b.cost_with_quarries(n_player_quarries) - price_reduction
            if n_doubloons >= price:
                buildings_with_reduction.append(
                    (str(b), price)
                )

        # any options
        if buildings_with_reduction:

            # Only take unique buildings
            (chosen_building, price) = player.choose_building(
                list(set(buildings_with_reduction))
            )
            if chosen_building is not None:
                i_chosen = game.available_buildings.index(chosen_building)
                building_to_add = game.available_buildings.pop(i_chosen)
                player.recieve_city_tile(building_to_add)

                # Take the money
                player.remove_doubloons(price)
    def __str__(self):
        return 'builder'

class Mayor(AbstractRole):
    '''
    Deliver the colonists on the ship
    '''
    def need_all_players(self):
        return True
    def play_with_all_players(self, players, game):

        colonists_to_deliver = game.colonist_portal.get_colonists_from_ship()
        for (i, player) in enumerate(players):
            col_to_player = colonists_to_deliver[i]
            if i == 0:
                super().get_stored_doubloons(player)
                # May get extra colonists from supply
                if player.wants_colonist_from_supply():
                    col_supply = game.colonist_portal.get_colonist_from_supply()
                    col_to_player.append(col_supply)

            player.recieve_colonists(col_to_player)

        # Reload the colonist ship
        colonists_to_reload = 0
        for player in players:
            colonists_to_reload += player.get_empty_city_spaces()

        # May not be enough
        game.colonist_portal.fill_ship(colonists_to_reload)
    def __str__(self):
        return 'mayor'

class Craftsman(AbstractRole):
    def need_all_players(self):
        return True
    def play_with_all_players(self, players, game):

        for (i, player) in enumerate(players):
            if i == 0:
                super().get_stored_doubloons(player)
            player_capacity = player.get_production_capacity()

            for good in definitions.ALL_GOODS:
                n_goods_produced = min(
                    player_capacity[good],
                    len(game.available_goods[good])
                )

                produced_goods = [
                    game.available_goods[good].pop()
                    for j in range(n_goods_produced)
                ]
                if produced_goods:
                    player.recieve_goods(produced_goods)

        # Additional single good from supply
        player_capacity = players[0].get_production_capacity()
        good_options = [
            good for good in definitions.ALL_GOODS if
            min(player_capacity[good], len(game.available_goods[good])) > 0
        ]
        if good_options:
            good_type = players[0].choose_good(good_options)
            good = game.available_goods[good_type].pop()
            players[0].recieve_goods([good])

    def __str__(self):
        return 'craftsman'
