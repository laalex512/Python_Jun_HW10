class Animal:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return f'{self.name} вес = {self.weight} кг'

    def move(self):
        pass
