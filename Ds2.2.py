# ✔ Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация
# данных), которые вы уже решали.
# ✔ Превратите функции в методы класса, а параметры в свойства.
# ✔ Задачи должны решаться через вызов методов экземпляра.


import json


class CsvFile:
    def __init__(self, name):
        self.name = name


    def convert(self):
        data = {}
        with open(self.name, encoding='UTF-8') as f1:
            for line in f1.readlines()[1:]:
                level, access_id, name = line.strip().split()
                name = name.capitalize()
                data[access_id] = [level, name]
        with open('res3.json', 'w', encoding='UTF-8') as f2:
            json.dump(data, f2, ensure_ascii=False)


CsvFile('res3.csv').convert()
