class AbstractBuilding:
    def __init__(self, colonist_capacity, space):
        # Fill with colonists
        self.occupation = []
        self.colonist_capacity = colonist_capacity
        self.space = space

    def add_colonist(self, colonist):
        '''
        Assume building not occupied
        '''
        if len(self.occupation) < self.colonist_capacity:
            self.occupation.append(colonist)
        else:
            raise ValueError('Incorrect')
    def add_colonists(self, colonists):
        '''
        Expects a list of colonists
        '''
        if  (len(colonists) + len(self.occupation)) <= self.colonist_capacity:
            self.occupation.extend(colonists)
        else:
            raise ValueError('Incorrect')

    def get_number_of_non_occupied_spaces(self):
        return self.colonist_capacity - len(self.occupation)

    def get_number_of_colonists(self):
        return len(self.occupation)

    def take_colonist(self):
        if self.occupation:
            return self.occupation.pop()
        else:
            raise ValueError('No colonist to take.')
    def get_state(self):
        return {
            'occupancy' : len(self.occupation),
            'capacity' : self.colonist_capacity
        }

    def __eq__(self, other):
        if str(self) == str(other):
            return True
        else:
            return False

class AbstractCityBuilding(AbstractBuilding):
    def __init__(self, colonist_capacity, cost, vp, quarries, space=1):

        self.cost = cost
        self.victory_points = vp
        self.quarries = quarries

        super().__init__(
            colonist_capacity,
            space
        )

    def cost_with_quarries(self, n_quarries):
        # Quarries can be saturated
        if n_quarries > self.quarries:
            cost = self.cost - self.quarries
        else:
            cost = self.cost - n_quarries
        return cost

class ProductionBuilding(AbstractCityBuilding):
    def __init__(self, good_type, colonist_capacity, cost, vp, quarries, space=1):
        # All production buildings take two space
        self.good_type = good_type
        super().__init__(
            colonist_capacity,
            cost,
            vp,
            quarries,
            space
        )

class IndigoPlant(ProductionBuilding):

    def __init__(self):
        super().__init__(
            'indigo', 3, 3, 2, 2
        )
    def __str__(self):
        return 'indigo_plant'

class SmallIndigoPlant(ProductionBuilding):
    def __init__(self):
        super().__init__('indigo', 1, 1, 1, 1)
    def __str__(self):
        return 'small_indigo_plant'

class SugarMill(ProductionBuilding):
    def __init__(self):
        super().__init__('sugar', 3, 4, 2, 2)
    def __str__(self):
        return 'sugar_mill'

class SmallSugarMill(ProductionBuilding):
    def __init__(self):
        super().__init__('sugar', 1, 2, 1, 1)
    def __str__(self):
        return 'small_sugar_mill'

class TobaccoStorage(ProductionBuilding):
    def __init__(self):
        super().__init__('tobacco', 3, 5, 3, 3)
    def __str__(self):
        return 'tobacco_storage'

class CoffeeRoaster(ProductionBuilding):
    def __init__(self):
        super().__init__('coffee', 2, 6, 3, 3)
    def __str__(self):
        return 'coffee_roaster'

class SmallMarket(AbstractCityBuilding):
    def __init__(self):
        self.phase = 'trader'
        super().__init__(1, 1, 1, 1)
    def __str__(self):
        return 'small_market'

class Hacienda(AbstractCityBuilding):
    def __init__(self):
        self.phase = 'trader'
        super().__init__(1, 2, 1, 1)
    def __str__(self):
        return 'hacienda'

class ConstructionHut(AbstractCityBuilding):
    def __init__(self):
        self.phase = 'trader'
        super().__init__(1, 2, 1, 1)
    def __str__(self):
        return 'construction_hut'

class SmallWarehouse(AbstractCityBuilding):
    def __init__(self):
        self.phase = 'trader'
        super().__init__(1, 3, 1, 1)
    def __str__(self):
        return 'small_warehouse'

class Hospice(AbstractCityBuilding):
    def __init__(self):
        self.phase = 'trader'
        super().__init__(1, 4, 2, 2)
    def __str__(self):
        return 'hospice'

class Office(AbstractCityBuilding):
    def __init__(self):
        self.colonist_capacity = 1
        self.phase = 'trader'
        super().__init__(1, 5, 2, 2)
    def __str__(self):
        return 'office'

class LargeMarket(AbstractCityBuilding):
    def __init__(self):
        self.phase = 'trader'
        super().__init__(1, 5, 2, 2)
    def __str__(self):
        return 'large_market'

class LargeWarehouse(AbstractCityBuilding):
    def __init__(self):
        self.phase = 'trader'
        super().__init__(1, 6, 2, 2)
    def __str__(self):
        return 'large_warehouse'

class Factory(AbstractCityBuilding):
    def __init__(self):
        self.phase = 'trader'
        super().__init__(1, 7, 3, 3)
    def __str__(self):
        return 'factory'

class University(AbstractCityBuilding):
    def __init__(self):
        self.phase = 'trader'
        super().__init__(1, 8, 3, 3)
    def __str__(self):
        return 'university'

class Harbor(AbstractCityBuilding):
    def __init__(self):
        self.phase = 'captain'
        super().__init__(1, 8, 3, 3)
    def __str__(self):
        return 'harbor'

class Wharf(AbstractCityBuilding):
    def __init__(self):
        self.phase = 'captain'
        super().__init__(1, 9, 3, 3)
    def __str__(self):
        return 'wharf'

class GuildHall(AbstractCityBuilding):
    def __init__(self):
        super().__init__(1, 10, 4, 4, space=2)
    def __str__(self):
        return 'guild_hall'

class Residence(AbstractCityBuilding):
    def __init__(self):
        super().__init__(1, 10, 4, 4, space=2)
    def __str__(self):
        return 'residence'

class Fortress(AbstractCityBuilding):
    def __init__(self):
        super().__init__(1, 10, 4, 4, space=2)
    def __str__(self):
        return 'fortress'

class CustomsHouse(AbstractCityBuilding):
    def __init__(self):
        super().__init__(1, 10, 4, 4, space=2)
    def __str__(self):
        return 'customs_house'

class CityHall(AbstractCityBuilding):
    def __init__(self):
        super().__init__(1, 10, 4, 4, space=2)
    def __str__(self):
        return 'city_hall'
