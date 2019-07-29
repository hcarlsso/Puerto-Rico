import random
from . import Buildings

class Portal:
    '''
    Class to handle colonists actions
    '''
    def __init__(self, n_show, quarries, plantations):

        self.n_show = n_show
        self.quarries = quarries
        self.plantations = plantations
        self.on_display = []
        self.discarded = []

    def fill_display(self):
        '''
        Randomly select plantations  for display.
        '''
        # Save the old ones
        self.discarded.extend(self.on_display)

        # Select items
        n_plantations = len(self.plantations)

        indeces = random.sample(list(range(n_plantations)), k=self.n_show)

        self.on_display = [
            p for (i, p) in enumerate(self.plantations) if i in indeces
        ]
        self.plantations = [
            p for (i, p) in enumerate(self.plantations) if i not in indeces
        ]

    def play_selection(self, player, quarry_option=False):

        options = self.on_display
        if quarry_option:
            quarry = self.quarries.pop()
            options.append(quarry)

        remaining = player.choose_plantation(options)
        if quarry_option and remaining[-1] == Quarry():
            # Give back quarry
            quarry = remaining.pop()
            self.quarries.append(quarry)

        self.on_display = remaining

    def take_quarry(self):
        return self.quarries.pop()

    def get_on_display(self):
        # Empty the display when selecting
        temp = self.on_display
        self.on_display = []
        return temp

    def return_unselected(self, unused):
        self.plantations.extend(unused)

    def get_state(self):

        return {
            'plantations' : len(self.plantations),
            'quarries' : len(self.quarries),
            'on_display' : sorted([str(p) for p in self.on_display])
        }

class IslandTile(Buildings.AbstractBuilding):

    def __init__(self):
        super().__init__(1, 1)
class Quarry(IslandTile):
    def __init__(self):
        super().__init__()
    def __str__(self):
        return 'quarry'
class Coffee(IslandTile):
    def __init__(self):
        super().__init__()
    def __str__(self):
        return 'coffee'
class Tobacco(IslandTile):
    def __init__(self):
        super().__init__()
    def __str__(self):
        return 'tobacco'
class Corn(IslandTile):
    def __init__(self):
        super().__init__()
    def __str__(self):
        return 'corn'
class Sugar(IslandTile):
    def __init__(self):
        super().__init__()
    def __str__(self):
        return 'sugar'
class Indigo(IslandTile):
    def __init__(self):
        super().__init__()
    def __str__(self):
        return 'indigo'
