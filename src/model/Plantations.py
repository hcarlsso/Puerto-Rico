import random

class Portal:

    def __init__(self, n_show, quarries, plantations):

        self.n_show = n_show
        self.quarries = quarries
        self.plantations = plantations
        self.on_display = []

    def fill_display(self):
        '''
        Randomly select plantations  for display.
        '''
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

class IslandTile:

    def __init__(self):
        self.filled = None

    def occupy(self, colonist):
        self.filled = colonist

    def get_state(self):
        state = {}
        if self.filled is None:
            state['occupied'] = False
        else:
            state['occupied'] = True
        return state

    def take_colonist(self):
        '''
        Return the colonist and empty the place
        '''
        temp = self.filled
        self.filled = None
        return temp

    def __eq__(self, other):

        if type(self) == type(other):
            return True
        else:
            return False

class Quarry(IslandTile):

    def __init__(self):
        pass

class Coffee(IslandTile):
    def __init__(self):
        super().__init__()
    def __str__(self):
        return 'Coffee'
class Tobacco(IslandTile):
    def __init__(self):
        super().__init__()
    def __str__(self):
        return 'Tobacco'
class Corn(IslandTile):
    def __init__(self):
        super().__init__()
    def __str__(self):
        return 'Corn'
class Sugar(IslandTile):
    def __init__(self):
        super().__init__()
    def __str__(self):
        return 'Sugar'
class Indigo(IslandTile):
    def __init__(self):
        super().__init__()
    def __str__(self):
        return 'Indigo'
