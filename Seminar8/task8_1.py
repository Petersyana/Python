"""
1) Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

my_message_list = list()  # создаем пустой список для ввода строк

# функция для заполнения списка строками, добавления списка в файл и вывода списка на печать


def my_text(my_message):
    # добавляем в список каждую новую введенную строку
    my_message_list.append(my_message)
    if my_message != '':
        return (my_text(my_message=input(f'Введите строку текста. Для завершения ввода - нажмите ENTER\n')))
    else:
        with open('text.txt', 'w', encoding='utf-8') as text:  # записываем список в файл
            for el in my_message_list:
                text.write(f'{el} \n')

        with open('text.txt', 'r', encoding='utf-8') as text:  # считываем из файла
            content = text.read()
        print(f'Ввод окончен')
        print(content)
        return


my_text(my_message=input(
    f'Введите строку текста. Для завершения ввода - нажмите ENTER\n'))
