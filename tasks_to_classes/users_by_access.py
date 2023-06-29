'''Напишите функцию, которая в бесконечном цикле
запрашивает имя, личный идентификатор и уровень
доступа (от 1 до 7).
После каждого ввода добавляйте новую информацию в
JSON файл.
Пользователи группируются по уровню доступа.
Идентификатор пользователя выступает ключём для имени.
Убедитесь, что все идентификаторы уникальны независимо
от уровня доступа.
При перезапуске функции уже записанные в файл данные
должны сохраняться.
'''

import copy
import csv
import json
from pathlib import Path


class UsersByAccess:
    __TITLE = ['Level access', 'ID', 'Name']
    __EMPTY_DICT = {
        "1": {},
        "2": {},
        "3": {},
        "4": {},
        "5": {},
        "6": {},
        "7": {},
    }

    def __init__(self, file_path: Path):
        self.current_dict = copy.deepcopy(self.__EMPTY_DICT)
        self.file_path = file_path
        if file_path.suffix == '.json':
            self.__read_from_json()
        elif file_path.suffix == '.csv':
            self.__read_from_csv()
        else:
            print('Unknown file format')

    def __is_valid(self, user_id):
        for level in self.current_dict.values():
            if user_id in level.keys():
                print(f'{user_id} is not unique ID')
                return False
        return True

    def ask_data(self):
        flag_continue = True
        while flag_continue:
            input_data = input("Enter user, ID, access level(1-7): ")
            if input_data == 'q':
                flag_continue = False
            else:
                user, user_id, level = input_data.split(', ')
                if self.__is_valid(user_id):
                    self.current_dict[level][user_id] = user

    def write_data(self):
        if self.file_path.suffix == '.json':
            self.__write_to_json()
        else:
            self.__write_to_csv()

    # json

    def __read_from_json(self):
        if self.file_path.is_file():
            with open(self.file_path, 'r', encoding='utf-8') as f:
                self.current_dict = json.load(f)

    def __write_to_json(self):
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(self.current_dict, f, ensure_ascii=False, indent=2)

    # csv

    def __read_from_csv(self):
        if self.file_path.is_file():
            with open(self.file_path, 'r', encoding='utf-8') as f:
                csv_read = csv.reader(f)
                next(csv_read)
                for line in csv_read:
                    if not line:  # проверка на пустую строку
                        self.current_dict[line[0]][line[1]] = line[2]

    def __write_to_csv(self):
        with open(self.file_path, 'w', encoding='utf-8') as f:
            output_data = [self.__TITLE]
            for level, mini_dict in self.current_dict.items():
                for user_id, user in mini_dict.items():
                    output_data.append([level, user_id, user])
            csv_write = csv.writer(f, dialect='excel', lineterminator='\n')
            csv_write.writerows(output_data)
