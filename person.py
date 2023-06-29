'''Напишите класс для хранения информации о человеке:
ФИО, возраст и т.п. на ваш выбор.
У класса должны быть методы birthday для увеличения
возраста на год, full_name для вывода полного ФИО и т.п. на
ваш выбор.
Убедитесь, что свойство возраст недоступно для прямого
изменения, но есть возможность получить текущий возраст.'''


class Person:
    def __init__(self, full_name, age, city='Minsk'):
        self.full_name = full_name
        self.__age = age
        self.city = city

    def birthday(self):
        self.__age += 1

    def get_full_name(self):
        return self.full_name

    def get_age(self):
        return self.__age

# person1 = Person('Alex Lisovsky', 39)
#
# person1.birthday()
# person1.birthday()
# person1.get_age()
# person1.get_full_name()
# print(person1.city)
