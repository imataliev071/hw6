class Hero:
    def __init__(self, name):
        self.name = name


class Hi(Hero):
    def __str__(self):
        return self.name

