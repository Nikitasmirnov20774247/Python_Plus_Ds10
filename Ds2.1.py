# ✔ Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация
# данных), которые вы уже решали.
# ✔ Превратите функции в методы класса, а параметры в свойства.
# ✔ Задачи должны решаться через вызов методов экземпляра.


from random import randint


class Guesser():
    def __init__(self, num, max_try):
        self.num = num
        self.max_try = max_try


    def check(self, guess):
        if guess < self.num:
            return 'Число больше'
        elif guess > self.num:
            return 'Число меньше'
        else:
            return False


    def run(self):
        print('\nУгадайте загаданное число (от 1 до 100)')
        for i in range(self.max_try):
            try:
                print(f'\nОставшееся число попыток: {self.max_try - i}')
                guess_num = int(input(f"Введите целое число: "))
                check_guess = self.check(guess_num)
                if check_guess:
                    print(check_guess)
                else:
                    return f"\nВы угадали! Это число {self.num}.\
                             \nВам понадобилось {i + 1} попыток из {self.max_try}"
            except:
                print('!! Введено некорректное значение !!')
                continue
        else:
            return f"\nВы потратили все попытки и не отгадали число {self.num}!"


if __name__ == "__main__":
    guess_game = Guesser(randint(1, 100), randint(3, 10))
    game_result = guess_game.run()
    print(game_result)
