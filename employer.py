'''Создайте класс Сотрудник.
Воспользуйтесь классом человека из прошлого задания.
У сотрудника должен быть:
○ шестизначный идентификационный номер
○ уровень доступа вычисляемый как остаток от деления
суммы цифр id на семь
'''
import random

from person import Person


class Employer(Person):
    __DIV_LEVEL = 7
    __ID_LENGTH = 6

    def __init__(self, *args, **kwargs):
        self.id_num = self.id_generate()
        self.access_level = self.level_calc()
        Person.__init__(self, *args, **kwargs)

    def id_generate(self):
        min_digits = int('1' + '0' * (self.__ID_LENGTH - 1))
        max_digits = int('1' + '0' * self.__ID_LENGTH)
        return random.randint(min_digits, max_digits)

    def level_calc(self):
        digits_sum = 0
        for i in str(self.id_num):
            digits_sum += int(i)
        return digits_sum % self.__DIV_LEVEL


employer1 = Employer('Alex Lisovsky', 39)
print(employer1.get_full_name())
print(employer1.get_age())
print(employer1.city)
print(employer1.id_num)
print(employer1.access_level)
