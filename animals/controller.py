from animal_classes.fish import Fish
from animal_classes.bird import Bird
from animal_classes.mammal import Mammal
from animal_classes.insect import Insect
import animals_factory as af


class Controller:

    def create_animals(self):
        fish1 = Fish(50, 'Карп', 5)
        bird1 = Bird('красный', 'Попугай', 1)
        mammal1 = Mammal(True, 'Медведь', 300)
        insect1 = Insect(False, 8, 'Паук', 0.05)

        print(fish1, bird1, mammal1, insect1, sep='\n')

    def factory_creater(self):
        af1 = af.AnimalFactory()
        fish1 = af1.create_animal(Fish, 50, 'Карп', 5)
        bird1 = af1.create_animal(Bird, 'красный', 'Попугай', 1)
        mammal1 = af1.create_animal(Mammal, True, 'Медведь', 300)
        insect1 = af1.create_animal(Insect, False, 8, 'Паук', 0.05)

        print(fish1, bird1, mammal1, insect1, sep='\n')
