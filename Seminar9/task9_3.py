"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""


class ErrorElement(Exception):  # класс-исключение
    def __init__(self, text):
        self.text = text


def my_stop(stop_input):  # функция для проверки завершения ввода чисел
    if stop_input == 'Y' or stop_input == 'y':
        return my_element(number=input('Введите число - '))
    else:
        print(f'Ввод окончен')
        quit()


def my_element(number, list_element=[]):  # функция для добавления чисел в список
    try:
        if number.isnumeric() == False:  # проверка на исключение
            raise ErrorElement(
                'ОШИБКА! Введено не число! В список не добавляется!')
        while True:
            list_element.append(number)  # добавляем число в список
            print(f'Текущий список - {list_element} \n ')  # печатаем список
            my_stop(stop_input=input(f'Продолжать ввод? Y/N '))
    except ErrorElement as err:
        print(err)  # печать текста исключения
        print(f'Текущий список - {list_element} \n ')  # печатаем список
        my_stop(stop_input=input(f'Продолжать ввод? Y/N '))


my_element(number=input('Введите число - '))
