# ✔ Доработать задачи 5-6. Создайте класс-фабрику.
# * Класс принимает тип животного (название одного из созданных классов)
# и параметры для этого типа.
# * Внутри класса создайте экземпляр на основе переданного типа и
# верните его из класса-фабрики.


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def get_name(self):
        return self.name
    

    def get_age(self):
        return self.age


class Horse(Animal):
    def __init__(self, name, age, power):
        super().__init__(name, age)
        self.power = power


    def get_name(self):
        return 'Secret!'


    def get_power(self):
        return self.power


class Fish(Animal):
    def __init__(self, name, age, tail_length):
        super().__init__(name, age)
        self.tail_length = tail_length


    def get_tail_length(self):
        return self.tail_length
    

class Bird(Animal):
    def __init__(self, name, age, fly_speed):
        super().__init__(name, age)
        self.fly_speed = fly_speed


    def get_fly_speed(self):
        return self.fly_speed


class Animalmaker:
    def __init__(self, animal_type: Animal, name, age, extra):
        self.animal_type = animal_type
        self.name = name
        self.age = age
        self.extra = extra


    def make_class(self):
        tmp = self.animal_type(self.name, self.age, self.extra)
        return tmp


a1 = Animalmaker(Bird, 'Zhenya', 6, 83).make_class()
print(a1.get_name())
print(a1.get_age())
print(a1.get_fly_speed())
a2 = Animalmaker(Horse, 'Lamborghini', 4, 75).make_class()
print(a2.get_name())
print(a2.get_age())
print(a2.get_power())
a3 = Animalmaker(Fish, 'Coral', 2, 9).make_class()
print(a3.get_name())
print(a3.get_age())
print(a3.get_tail_length())
