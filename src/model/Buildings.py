class AbstractBuilding:
    pass
class ProductionBuilding(AbstractBuilding):
    pass
class IndigoPlant(ProductionBuilding):

    def __init__(self):

        self.victory_points = 2
        self.cost = 3

        # Production units
        self.production_units = 3
        self.occupation = 0
        self.good_type = 'indigo'

class SmallMarket(AbstractBuilding):
    def __init__(self):
        self.victory_points = 1
        self.cost = 1
