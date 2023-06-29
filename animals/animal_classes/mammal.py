from .animal import Animal


class Mammal(Animal):
    def __init__(self, is_predator: bool, *args, **kwargs):
        self.is_predator = is_predator
        super().__init__(*args, **kwargs)

    def move(self):
        return 'бегает'

    def feeding_method(self):
        if self.is_predator:
            return "хищник"
        else:
            return 'травоядное'

    def __str__(self):
        return f'{super().__str__()} {self.move()} {self.feeding_method()}'
