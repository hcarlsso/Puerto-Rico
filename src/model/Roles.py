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
    def play(self, player, game, privilege=False):
        super().get_stored_doubloons(player)
        # Get extra victory point for first kind of good shipped
        pass
    def __str__(self):
        return 'captain'

class Trader(AbstractRole):
    def play(self, player, game, privilege=False):
        super().get_stored_doubloons(player)
        # Get extra doublon when selling
        pass
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
    def play(self, player, game, privilege=False):
        if privilege:
            super().get_stored_doubloons(player)
            # Can take quarry instead
            quarry_option=True
        else:
            quarry_option=False

        game.tiles_portal.play_selection(
            player,
            quarry_option=quarry_option
        )
    def __str__(self):
        return 'settler'

class Builder(AbstractRole):
    def play(self, player, game, privilege=False):
        super().get_stored_doubloons(player)
        # Get reduction in price
        pass
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
    def play(self, player, game, privilege=False):
        super().get_stored_doubloons(player)
        # Additional good from supply
        pass
    def __str__(self):
        return 'craftsman'
