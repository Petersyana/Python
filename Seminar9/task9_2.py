"""
Задание 2.

Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class DivideByZero:
    def __init__(self, text):
        self.text = text

    dividend = float(input(f'Введите делимое - '))  # делимое

    try:
        divider = float(input(f'Введите делитель - '))  # делитель
        result = dividend / divider  # частное
    except ZeroDivisionError:
        print("На ноль делить нельзя!")
        quit()

    print(result)