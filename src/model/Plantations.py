import random

class Portal:

    def __init__(self, N_show, quarries, plantations):

        self.N_show = N_show
        self.quarries = quarries
        self.plantations = plantations
        self.on_display = []

    def fill_display(self):

        # Select items
        N_plantations = len(self.plantations)

        indeces = random.sample(list(range(N_plantations)), k = self.N_show)

        self.on_display = [p for (i, p) in enumerate(self.plantations) if i in indeces]
        self.plantations = [p for (i, p) in enumerate(self.plantations) if i not in indeces]

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

    def take_colonist(self):
        # Return the colonist and empty the place
        temp = self.filled
        self.filled = None
        return temp

class Quarry(IslandTile):

    def __init__(self):
        pass

class PlantationTile(IslandTile):

    def __eq__(self, other):

        if type(self) == type(other):
            return True
        else:
            return False

class Coffee(PlantationTile):
    def __init__(self):
        super().__init__()
    def __str__(self):
        return 'Coffee'
class Tobacco(PlantationTile):
    def __init__(self):
        super().__init__()
    def __str__(self):
        return 'Tobacco'
class Corn(PlantationTile):
    def __init__(self):
        super().__init__()
    def __str__(self):
        return 'Corn'
class Sugar(PlantationTile):
    def __init__(self):
        super().__init__()
    def __str__(self):
        return 'Sugar'
class Indigo(PlantationTile):
    def __init__(self):
        super().__init__()
    def __str__(self):
        return 'Indigo'
