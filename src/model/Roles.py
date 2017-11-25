class AbstractRole:
    def __init__(self):
        self.doublons = 0
    def __str__(self):
        return self.__class__.__name__ + " doublons: {:d}".format(self.doublons)

    def add_doublon(self):
        self.doublons += 1

class Captain(AbstractRole):
    def __init__(self):
        super().__init__()

class Trader(AbstractRole):
    def __init__(self):
        super().__init__()

class Prospector(AbstractRole):
    def __init__(self):
        super().__init__()

class Settler(AbstractRole):
    def __init__(self):
        super().__init__()

class Builder(AbstractRole):
    def __init__(self):
        super().__init__()

class Mayor(AbstractRole):
    def __init__(self):
        super().__init__()

class Craftsman(AbstractRole):
    def __init__(self):
        super().__init__()
