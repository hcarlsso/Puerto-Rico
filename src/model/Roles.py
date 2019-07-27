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

class Captain(AbstractRole):
    def play_privilege(self):
        super().get_stored_doubloons(player)
        # Get extra victory point for first kind of good shipped
        pass
    def play_ordinary(self):
        # Ship one type
        pass
    def __str__(self):
        return 'captain'

class Trader(AbstractRole):
    def play_privilege(self):
        super().get_stored_doubloons(player)
        # Get extra doublon when selling
        pass
    def play_ordinary(self):
        # May sell in the trading house
        pass
    def __str__(self):
        return 'trader'

class Prospector(AbstractRole):
    def play_privilege(self, player, game_state):
        super().get_stored_doubloons(player)

        # Recieve 1 doubloon
        player.recieve_doubloons(1)

    def play_ordinary(self, player, game_state):
        # Nothing happens here
        pass
    def __str__(self):
        return 'prospector'

class Settler(AbstractRole):
    def play_privilege(self, player, game_state):
        super().get_stored_doubloons(player)
        # Can take quarry instead
        game_state.tiles_portal.play_selection(
            player,
            quarry_option = True
        )
    def play_ordinary(self, player, game_state):
        # Each player takes plantation
        # Default cannot take quarry
        game_state.tiles_portal.play_selection(
            player,
            quarry_option = False
        )
    def __str__(self):
        return 'settler'

class Builder(AbstractRole):
    def play_privilege(self):
        super().get_stored_doubloons(player)
        # Get reduction in price
        pass
    def play_ordinary(self):
        # Buy a building
        pass
    def __str__(self):
        return 'builder'

class Mayor(AbstractRole):
    def play_privilege(self):
        super().get_stored_doubloons(player)
        # Get additional colonist from supply
        pass
    def play_ordinary(self):
        # Take one colonist
        pass
    def __str__(self):
        return 'mayor'

class Craftsman(AbstractRole):
    def play_privilege(self):
        super().get_stored_doubloons(player)
        # Additional good from supply
        pass
    def play_ordinary(self):
        # Take goods
        pass
    def __str__(self):
        return 'craftsman'
