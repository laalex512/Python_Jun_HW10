from .animal import Animal


class Bird(Animal):
    def __init__(self, color, *args, **kwargs):
        self.color = color
        super().__init__(*args, **kwargs)

    def move(self):
        return 'летает'

    def __str__(self):
        return f'{super().__str__()} {self.move()} цвет: {self.color}'
