"""
Задание 4. Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75
Решите через рекурсию. В задании нельзя применять циклы.
Нужно обойтисть без создания массива!
"""


"""
    amount_element -количество элементов, которое водит пользователь
    amount_temp - для вывода количества элементов на печать
    sum_amount - сумма элементов
    element - элемент, начинаем с 1
"""

def sum(amount_element, sum_amount = 0, element = 1, amount_temp = 0):
    if amount_element == 0:
        print(f'Количество элементов - {amount_temp}, их сумма - {sum_amount}')
        return
    else:
        sum_amount = sum_amount + element
        element_element = element_element / -2
        amount_temp += 1
        return sum(amount_element-1, sum_amount, element, amount_temp)

sum(amount=int(input('Введите количество элементов n= ')))
