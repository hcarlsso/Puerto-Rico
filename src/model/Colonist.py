class Portal:
    '''
    The class to handle all colonist matters.
    '''
    def __init__(self, ship, supply):

        self.ship = ship
        self.supply = supply

    def fill_ship(self, N_colonists_request):

        # if requested is higher than existing
        if N_colonists_request > len(self.supply):
            N_colonists = len(self.supply)
        else:
            N_colonists = N_colonists_request

        self.ship.fill_colonists(self.supply[:N_colonists])
        # Remove from supply
        del self.supply[:N_colonists]

    def empty_ship(self):

        return self.ship.iterator_colonists()

    def get_state(self):
        return {
            'ship' : len(self.ship.loaded_colonists),
            'supply' : len(self.supply)
        }
    def is_game_over(self):
        return not self.supply # No more colonist

class Colonist:
    def __init__(self):
        pass

class Ship:
    def __init__(self):

        self.loaded_colonists = []

    def fill_colonists(self, colonists):
        # It should be empty
        if self.loaded_colonists == []:
            self.loaded_colonists.extend(colonists)
        else:
            raise ValueError('Colonist ship is not empty')

    def iterator_colonists(self):
        for colonist in self.loaded_colonists:
            yield colonist

        # Empty the ship
        self.loaded_colonists = []
