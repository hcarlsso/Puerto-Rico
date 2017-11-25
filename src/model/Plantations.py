class IslandTile:

    pass

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
        pass

class Tobacco(PlantationTile):
    def __init__(self):
        pass

class Corn(PlantationTile):
    def __init__(self):
        pass

class Sugar(PlantationTile):
    def __init__(self):
        pass

class Indigo(PlantationTile):
    def __init__(self):
        pass
