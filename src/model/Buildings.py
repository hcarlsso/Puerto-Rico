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
        self.quarries = 2

        # Production units
        self.production_units = 3
        self.good_type = 'indigo'
        super().__init__()

    def __str__(self):
        return 'Indigo Plant'
class SmallIndigoPlant(ProductionBuilding):
    def __init__(self):
        self.victory_points = 1
        self.cost = 1
        self.quarries = 1

        # Production units
        self.production_units = 1
        self.good_type = 'indigo'
        super().__init__()

    def __str__(self):
        return 'Small Indigo Plant'
class SugarMill(ProductionBuilding):
    def __init__(self):
        self.victory_points = 2
        self.cost = 4
        self.quarries = 2
        # Production units
        self.production_units = 3
        self.good_type = 'sugar'
        super().__init__()
    def __str__(self):
        return 'Sugar Mill'
class SmallSugarMill(ProductionBuilding):
    def __init__(self):
        self.victory_points = 1
        self.cost = 2
        self.quarries = 1
        # Production units
        self.production_units = 1
        self.good_type = 'sugar'
        super().__init__()
    def __str__(self):
        return 'Small Sugar Mill'
class TobaccoStorage(ProductionBuilding):
    def __init__(self):
        self.victory_points = 3
        self.cost = 5
        self.quarries = 3
        # Production units
        self.production_units = 3
        self.good_type = 'tobacco'
        super().__init__()
    def __str__(self):
        return 'Tobacco Storage'
class CoffeeRoaster(ProductionBuilding):
    def __init__(self):
        self.victory_points = 3
        self.cost = 6
        self.quarries = 3
        # Production units
        self.production_units = 2
        self.good_type = 'coffee'
        super().__init__()
    def __str__(self):
        return 'Coffee Roaster'

class SmallMarket(AbstractBuilding):
    def __init__(self):
        self.victory_points = 1
        self.cost = 1
        self.quarries = 1
        self.phase = 'trader'
    def __str__(self):
        return 'Small Market'

class Hacienda(AbstractBuilding):
    def __init__(self):
        self.victory_points = 1
        self.cost = 2
        self.quarries = 1
        self.phase = 'trader'
    def __str__(self):
        return 'Hacienda'

class ConstructionHut(AbstractBuilding):
    def __init__(self):
        self.victory_points = 1
        self.cost = 2
        self.quarries = 1
        self.phase = 'trader'
    def __str__(self):
        return 'Construction Hut'
class SmallWarehouse(AbstractBuilding):
    def __init__(self):
        self.victory_points = 1
        self.cost = 3
        self.quarries = 1
        self.phase = 'trader'
    def __str__(self):
        return 'Small Warehouse'
class Hospice(AbstractBuilding):
    def __init__(self):
        self.victory_points = 2
        self.cost = 4
        self.quarries = 2
        self.phase = 'trader'
    def __str__(self):
        return 'Hospice'

class Office(AbstractBuilding):
    def __init__(self):
        self.victory_points = 2
        self.cost = 5
        self.quarries = 2
        self.phase = 'trader'
    def __str__(self):
        return 'Office'
class LargeMarket(AbstractBuilding):
    def __init__(self):
        self.victory_points = 2
        self.cost = 5
        self.quarries = 2
        self.phase = 'trader'
    def __str__(self):
        return 'Large Market'

class LargeWarehouse(AbstractBuilding):
    def __init__(self):
        self.victory_points = 2
        self.cost = 6
        self.quarries = 2
        self.phase = 'trader'
    def __str__(self):
        return 'Large Warehouse'
class Factory(AbstractBuilding):
    def __init__(self):
        self.victory_points = 3
        self.cost = 7
        self.quarries = 3
        self.phase = 'trader'
    def __str__(self):
        return 'Factory'

class University(AbstractBuilding):
    def __init__(self):
        self.victory_points = 3
        self.cost = 8
        self.quarries = 3
        self.phase = 'trader'
    def __str__(self):
        return 'University'

class Harbor(AbstractBuilding):
    def __init__(self):
        self.victory_points = 3
        self.cost = 8
        self.quarries = 3
        self.phase = 'captain'
    def __str__(self):
        return 'Harbor'

class Wharf(AbstractBuilding):
    def __init__(self):
        self.victory_points = 3
        self.cost = 9
        self.quarries = 3
        self.phase = 'captain'
    def __str__(self):
        return 'Wharf'

class GuildHall(AbstractBuilding):
    def __init__(self):
        self.victory_points = 4
        self.cost = 10
        self.quarries = 4
    def __str__(self):
        return 'Guild Hall'

class Residence(AbstractBuilding):
    def __init__(self):
        self.victory_points = 4
        self.cost = 10
        self.quarries = 4
    def __str__(self):
        return 'Residence'
class Fortress(AbstractBuilding):
    def __init__(self):
        self.victory_points = 4
        self.cost = 10
        self.quarries = 4
    def __str__(self):
        return 'Fortress'
class CustomsHouse(AbstractBuilding):
    def __init__(self):
        self.victory_points = 4
        self.cost = 10
        self.quarries = 4
    def __str__(self):
        return 'Customs House'
class CityHall(AbstractBuilding):
    def __init__(self):
        self.victory_points = 4
        self.cost = 10
        self.quarries = 4
    def __str__(self):
        return 'City Hall'
