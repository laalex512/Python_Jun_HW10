class AnimalFactory:

    def create_animal(self, animal_type, *args, **kwargs):
        return animal_type(*args, **kwargs)
