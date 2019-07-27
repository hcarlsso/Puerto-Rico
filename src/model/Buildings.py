class AbstractBuilding:
    def __init__(self):
        # Fill with colonists
        self.occupation = []

    def add_colonists(self, colonists):
        '''
        Expects a list of colonists
        '''
        if isinstance(colonists, list) and len(colonists) <= self.colonist_capacity:
            self.occupation.extend(colonists)
        else:
            raise ValueError('Incorrect')

class ProductionBuilding(AbstractBuilding):
    def __init__(self):
        # All production buildings take two space
        self.space = 2
        super().__init__()

    def get_state(self):
        return len(self.occupation)

class IndigoPlant(ProductionBuilding):

    def __init__(self):

        self.victory_points = 2
        self.cost = 3
        self.quarries = 2

        # Production units
        self.colonist_capacity = 3
        self.good_type = 'indigo'
        super().__init__()
    def __str__(self):
        return 'indigo_plant'

class SmallIndigoPlant(ProductionBuilding):
    def __init__(self):
        self.victory_points = 1
        self.cost = 1
        self.quarries = 1

        # Production units
        self.colonist_capacity = 1
        self.good_type = 'indigo'
        super().__init__()

    def __str__(self):
        return 'small_indigo_plant'

class SugarMill(ProductionBuilding):
    def __init__(self):
        self.victory_points = 2
        self.cost = 4
        self.quarries = 2
        # Production units
        self.colonist_capacity = 3
        self.good_type = 'sugar'
        super().__init__()
    def __str__(self):
        return 'sugar_mill'

class SmallSugarMill(ProductionBuilding):
    def __init__(self):
        self.victory_points = 1
        self.cost = 2
        self.quarries = 1
        # Production units
        self.colonist_capacity = 1
        self.good_type = 'sugar'
        super().__init__()
    def __str__(self):
        return 'small_sugar_mill'

class TobaccoStorage(ProductionBuilding):
    def __init__(self):
        self.victory_points = 3
        self.cost = 5
        self.quarries = 3
        # Production units
        self.colonist_capacity = 3
        self.good_type = 'tobacco'
        super().__init__()
    def __str__(self):
        return 'tobacco_storage'

class CoffeeRoaster(ProductionBuilding):
    def __init__(self):
        self.victory_points = 3
        self.cost = 6
        self.quarries = 3
        # Production units
        self.colonist_capacity = 2
        self.good_type = 'coffee'
        super().__init__()
    def __str__(self):
        return 'coffee_roaster'

class SmallMarket(AbstractBuilding):
    def __init__(self):
        self.space = 2
        self.victory_points = 1
        self.cost = 1
        self.quarries = 1
        self.colonist_capacity = 1
        self.phase = 'trader'
    def __str__(self):
        return 'small_market'

class Hacienda(AbstractBuilding):
    def __init__(self):
        self.space = 2
        self.victory_points = 1
        self.cost = 2
        self.quarries = 1
        self.colonist_capacity = 1
        self.phase = 'trader'
    def __str__(self):
        return 'hacienda'

class ConstructionHut(AbstractBuilding):
    def __init__(self):
        self.space = 2
        self.victory_points = 1
        self.cost = 2
        self.quarries = 1
        self.colonist_capacity = 1
        self.phase = 'trader'
    def __str__(self):
        return 'construction_hut'

class SmallWarehouse(AbstractBuilding):
    def __init__(self):
        self.space = 2
        self.victory_points = 1
        self.cost = 3
        self.quarries = 1
        self.colonist_capacity = 1
        self.phase = 'trader'
    def __str__(self):
        return 'small_warehouse'

class Hospice(AbstractBuilding):
    def __init__(self):
        self.space = 2
        self.victory_points = 2
        self.cost = 4
        self.quarries = 2
        self.colonist_capacity = 1
        self.phase = 'trader'
    def __str__(self):
        return 'hospice'

class Office(AbstractBuilding):
    def __init__(self):
        self.victory_points = 2
        self.cost = 5
        self.quarries = 2
        self.colonist_capacity = 1
        self.phase = 'trader'
    def __str__(self):
        return 'office'

class LargeMarket(AbstractBuilding):
    def __init__(self):
        self.space = 2
        self.victory_points = 2
        self.cost = 5
        self.quarries = 2
        self.colonist_capacity = 1
        self.phase = 'trader'
    def __str__(self):
        return 'large_market'

class LargeWarehouse(AbstractBuilding):
    def __init__(self):
        self.space = 2
        self.victory_points = 2
        self.cost = 6
        self.quarries = 2
        self.colonist_capacity = 1
        self.phase = 'trader'
    def __str__(self):
        return 'large_warehouse'

class Factory(AbstractBuilding):
    def __init__(self):
        self.space = 2
        self.victory_points = 3
        self.cost = 7
        self.quarries = 3
        self.colonist_capacity = 1
        self.phase = 'trader'
    def __str__(self):
        return 'factory'

class University(AbstractBuilding):
    def __init__(self):
        self.space = 2
        self.victory_points = 3
        self.cost = 8
        self.quarries = 3
        self.colonist_capacity = 1
        self.phase = 'trader'
    def __str__(self):
        return 'university'

class Harbor(AbstractBuilding):
    def __init__(self):
        self.space = 2
        self.victory_points = 3
        self.cost = 8
        self.quarries = 3
        self.colonist_capacity = 1
        self.phase = 'captain'
    def __str__(self):
        return 'harbor'

class Wharf(AbstractBuilding):
    def __init__(self):
        self.space = 2
        self.victory_points = 3
        self.cost = 9
        self.quarries = 3
        self.colonist_capacity = 1
        self.phase = 'captain'
    def __str__(self):
        return 'wharf'

class GuildHall(AbstractBuilding):
    def __init__(self):
        self.space = 4
        self.victory_points = 4
        self.cost = 10
        self.quarries = 4
        self.colonist_capacity = 1
    def __str__(self):
        return 'guild_hall'

class Residence(AbstractBuilding):
    def __init__(self):
        self.space = 4
        self.victory_points = 4
        self.cost = 10
        self.quarries = 4
        self.colonist_capacity = 1
    def __str__(self):
        return 'residence'

class Fortress(AbstractBuilding):
    def __init__(self):
        self.space = 4
        self.victory_points = 4
        self.cost = 10
        self.quarries = 4
        self.colonist_capacity = 1
    def __str__(self):
        return 'fortress'

class CustomsHouse(AbstractBuilding):
    def __init__(self):
        self.space = 4
        self.victory_points = 4
        self.cost = 10
        self.quarries = 4
        self.colonist_capacity = 1
    def __str__(self):
        return 'customs_house'

class CityHall(AbstractBuilding):
    def __init__(self):
        self.space = 4
        self.victory_points = 4
        self.cost = 10
        self.quarries = 4
        self.colonist_capacity = 1
    def __str__(self):
        return 'city_hall'
