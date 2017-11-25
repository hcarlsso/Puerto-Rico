class AbstractRole:
    def __str__(self):
        return self.__class__.__name__

class Captain(AbstractRole):
    def __init__(self):
        pass

class Trader(AbstractRole):
    def __init__(self):
        pass

class Prospector(AbstractRole):
    def __init__(self):
        pass


class Settler(AbstractRole):
    def __init__(self):
        pass

class Builder(AbstractRole):
    def __init__(self):
        pass

class Mayor(AbstractRole):
    def __init__(self):
        pass

class Craftsman(AbstractRole):
    def __init__(self):
        pass
