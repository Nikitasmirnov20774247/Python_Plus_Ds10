# ✔ Доработайте задачу 5.
# ✔ Вынесите общие свойства и методы классов в класс
# Животное.
# ✔ Остальные классы наследуйте от него.
# ✔ Убедитесь, что в созданные ранее классы внесены правки.


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
    def __init__(self, name, age, speed):
        super().__init__(name, age)
        self.speed = speed


    def get_speed(self):
        return self.speed
    

h1 = Horse('Blacky', 12, 'jump')

print(h1.get_name())
print(h1.get_age())
print(h1.get_power())
