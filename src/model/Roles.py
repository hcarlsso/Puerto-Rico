class AbstractRole:
    def __init__(self):
        self.doublons = 0
    def __str__(self):
        return self.__class__.__name__ + " doublons: {:d}".format(self.doublons)

    def add_doublon(self):
        self.doublons += 1

    def get_stored_doublons(self, player):
        # Make copy
        player.recieve_doublons(self.doublons)

        # Reset
        self.doublons = 0

class Captain(AbstractRole):
    def __init__(self):
        super().__init__()

    def play_privilege(self):
        # Get extra victory point for first kind of good shipped
        pass
    def play_ordinary(self):
        # Ship one type
        pass

class Trader(AbstractRole):
    def __init__(self):
        super().__init__()
    def play_privilege(self):
        # Get extra doublon when selling
        pass
    def play_ordinary(self):
        # May sell in the trading house
        pass

class Prospector(AbstractRole):
    def __init__(self):
        super().__init__()
    def play_privilege(self, player, game_state):
        super().get_stored_doublons(player)

        # Recieve 1 doublon
        player.recieve_doublons(1)

    def play_ordinary(self, player, game_state):
        # Nothing happens here
        pass

class Settler(AbstractRole):
    def __init__(self):
        super().__init__()
    def play_privilege(self, player, game_state):
        # Can take quarry instead
        pass
    def play_ordinary(self, player, game_state):
        # Each player takes plantation
        pass

class Builder(AbstractRole):
    def __init__(self):
        super().__init__()
    def play_privilege(self):
        # Get reduction in price
        pass
    def play_ordinary(self):
        # Buy a building
        pass

class Mayor(AbstractRole):
    def __init__(self):
        super().__init__()
    def play_privilege(self):
        # Get additional colonist from supply
        pass
    def play_ordinary(self):
        # Take one colonist
        pass

class Craftsman(AbstractRole):
    def __init__(self):
        super().__init__()
    def play_privilege(self):
        # Additional good from supply
        pass
    def play_ordinary(self):
        # Take goods
        pass
