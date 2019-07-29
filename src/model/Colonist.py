import math
class Portal:
    '''
    The class to handle all colonist matters.
    '''
    def __init__(self, ship, supply, n_players):

        self.ship = ship
        self.supply = supply
        self.n_players = n_players

    def fill_ship(self, n_colonists_request):

        # if requested is higher than existing
        if n_colonists_request > len(self.supply):
            n_colonists = len(self.supply)
        elif n_colonists_request < self.n_players:
            n_colonists = self.n_players
        else:
            n_colonists = n_colonists_request

        self.ship.fill_colonists(self.supply[:n_colonists])
        # Remove from supply
        del self.supply[:n_colonists]

    def empty_ship(self):

        return self.ship.iterator_colonists()

    def get_state(self):
        return {
            'ship' : len(self.ship.loaded_colonists),
            'supply' : len(self.supply)
        }
    def is_game_over(self):
        return not self.supply # No more colonist

    def get_colonists_from_ship(self):
        '''
        Get a list of lists
        '''
        # Should always be equal or larger than one
        n_base = math.floor(len(self.ship.loaded_colonists)/self.n_players)
        n_rest = int(math.fmod(len(self.ship.loaded_colonists), self.n_players))

        # The base number of colonists
        resp = []
        for ii in range(self.n_players):
            base_p = []
            for jj in range(n_base):
                col = self.ship.loaded_colonists.pop()
                base_p.append(col)
            resp.append(base_p)

        # The rest of the colonists
        for i in range(n_rest):
            col = self.ship.loaded_colonists.pop()
            resp[i].append(col)

        return resp

    def get_colonist_from_supply(self):
        '''
        Get one colonist from supply
        '''
        return self.supply.pop()
class Colonist:
    def __init__(self):
        pass
    def __str__(self):
        return 'colonist'

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
