class AbstractGood:
    def __eq__(self, other):
        if str(self) == str(other):
            return True
        else:
            return False

class Coffee(AbstractGood):
    def __init__(self):
        super().__init__()
    def __str__(self):
        return 'coffee'
class Tobacco(AbstractGood):
    def __init__(self):
        super().__init__()
    def __str__(self):
        return 'tobacco'
class Corn(AbstractGood):
    def __init__(self):
        super().__init__()
    def __str__(self):
        return 'corn'
class Sugar(AbstractGood):
    def __init__(self):
        super().__init__()
    def __str__(self):
        return 'sugar'
class Indigo(AbstractGood):
    def __init__(self):
        super().__init__()
    def __str__(self):
        return 'indigo'
