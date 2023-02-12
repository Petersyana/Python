"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""


class ErrorElement:
    def __init__(self, *args):
        self.list_element = []

    def my_element(self):

        while True:
            try:
                number = int(input('Введите число - '))
                self.list_element.append(number)  # добавляем число в список
                print(f'{self.list_element} \n ')  # печатаем список
            except:
                print(f"Ошибка ввода! Введено не число")
                stop_input = input(f'Повторить ввод? Y/N ')

                if stop_input == 'Y' or stop_input == 'y':
                    print(num.my_element())
                else:
                    return f'Ввод окончен'
                    quit()


num = ErrorElement(1)
print(num.my_element())
