class AbstractBuilding:
    def __init__(self):
        # Fill with colonists
        self.occupation = []

class ProductionBuilding(AbstractBuilding):
    def __init__(self):
        super().__init__()

    def get_state(self):
        return {}

class IndigoPlant(ProductionBuilding):

    def __init__(self):

        self.victory_points = 2
        self.cost = 3

        # Production units
        self.production_units = 3
        self.good_type = 'indigo'
        super().__init__()

class SmallIndigoPlant(ProductionBuilding):
    def __init__(self):
        self.victory_points = 1
        self.cost = 1

        # Production units
        self.production_units = 1
        self.good_type = 'indigo'
        super().__init__()
class SugarMill(ProductionBuilding):
    def __init__(self):
        self.victory_points = 2
        self.cost = 4

        # Production units
        self.production_units = 3
        self.good_type = 'sugar'
        super().__init__()
class SmallSugarMill(ProductionBuilding):
    def __init__(self):
        self.victory_points = 1
        self.cost = 2

        # Production units
        self.production_units = 1
        self.good_type = 'sugar'
        super().__init__()

class TobaccoStorage(ProductionBuilding):
    def __init__(self):
        self.victory_points = 3
        self.cost = 5

        # Production units
        self.production_units = 3
        self.good_type = 'tobacco'
        super().__init__()
class CoffeeRoaster(ProductionBuilding):
    def __init__(self):
        self.victory_points = 3
        self.cost = 6

        # Production units
        self.production_units = 2
        self.good_type = 'coffee'
        super().__init__()

class SmallMarket(AbstractBuilding):
    def __init__(self):
        self.victory_points = 1
        self.cost = 1
        self.phase = 'trader'

class Hacienda(AbstractBuilding):
    def __init__(self):
        self.victory_points = 1
        self.cost = 1
        self.phase = 'trader'

class ConstructionHut(AbstractBuilding):
    def __init__(self):
        self.victory_points = 1
        self.cost = 1
        self.phase = 'trader'
class SmallWarehouse(AbstractBuilding):
    def __init__(self):
        self.victory_points = 1
        self.cost = 1
        self.phase = 'trader'
class Hospice(AbstractBuilding):
    def __init__(self):
        self.victory_points = 1
        self.cost = 1
        self.phase = 'trader'
class Office(AbstractBuilding):
    def __init__(self):
        self.victory_points = 1
        self.cost = 1
        self.phase = 'trader'
class LargeMarket(AbstractBuilding):
    def __init__(self):
        self.victory_points = 1
        self.cost = 1
        self.phase = 'trader'
class LargeWarehouse(AbstractBuilding):
    def __init__(self):
        self.victory_points = 1
        self.cost = 1
        self.phase = 'trader'
class Factory(AbstractBuilding):
    def __init__(self):
        self.victory_points = 1
        self.cost = 1
        self.phase = 'trader'
class University(AbstractBuilding):
    def __init__(self):
        self.victory_points = 1
        self.cost = 1
        self.phase = 'trader'
class Harbor(AbstractBuilding):
    def __init__(self):
        self.victory_points = 1
        self.cost = 1
class Wharf(AbstractBuilding):
    def __init__(self):
        self.victory_points = 1
        self.cost = 1
class GuildHall(AbstractBuilding):
    def __init__(self):
        self.victory_points = 1
        self.cost = 1
class Residence(AbstractBuilding):
    def __init__(self):
        self.victory_points = 1
        self.cost = 1
class Fortress(AbstractBuilding):
    def __init__(self):
        self.victory_points = 1
        self.cost = 1
class CustomsHouse(AbstractBuilding):
    def __init__(self):
        self.victory_points = 1
        self.cost = 1
class CityHall(AbstractBuilding):
    def __init__(self):
        self.victory_points = 1
        self.cost = 1
