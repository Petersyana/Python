"""
Задание 2.

Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class DivideByZero(Exception):
    def __init__(self, text):
        self.text = text

dividend = float(input(f'Введите делимое - '))  # делимое
divider = float(input(f'Введите делитель - '))  # делитель      

try: 
    if divider == 0: 
        raise DivideByZero('ОШИБКА! Деление на 0!') 
    result = dividend / divider 
except DivideByZero as err: 
        print(err)
else: 
    print(f'Результат: {result}')

