from .animal import Animal


class Fish(Animal):
    def __init__(self, length, *args, **kwargs):
        self.length = length
        super().__init__(*args, **kwargs)

    def move(self):
        return 'плавает'

    def __str__(self):
        return f'{super().__str__()} {self.move()} длина: {self.length}'
