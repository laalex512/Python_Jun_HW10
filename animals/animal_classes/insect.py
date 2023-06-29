from .animal import Animal


class Insect(Animal):
    def __init__(self, is_flying: bool, count_limbs, *args, **kwargs):
        self.is_flying = is_flying
        self.count_limbs = count_limbs
        super().__init__(*args, **kwargs)

    def move(self):
        if self.is_flying:
            return 'летает'
        else:
            return 'ползает'

    def __str__(self):
        return f'{super().__str__()} {self.move()} конечностей: {self.count_limbs}'
