# ✔ Создайте класс прямоугольник.
# ✔ Класс должен принимать длину и ширину при создании
# экземпляра.
# ✔ У класса должно быть два метода, возвращающие периметр
# и площадь.
# ✔ Если при создании экземпляра передаётся только одна
# сторона, считаем что у нас квадрат.


import math


class Rectangle:
    def __init__(self, a, b = None):
        self.a = a
        self.b = a if not b else b
        # if not b:
        #     self.b = a
        # else:
        #     self.b = b


    def get_lenght(self):
        return 2 * (self.a + self.b)


    def get_area(self):
        return self.a * self.b


r1 = Rectangle(10, 5)
print(r1.get_lenght())
print(r1.get_area())
