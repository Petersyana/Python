"""
5. Сделайте профилирование кода любого или любых выполненных заданий
с помощью модуля timeit, опишите результат
"""

# используя функцию sort()
from timeit import timeit


def my_func_sort(a, b, c=0):
    list_1 = [a, b, c]
    list_1.sort()
    summa = b + c
    return summa

# без функции sort()


def my_func(a, b, c=0):
    summa = 0
    if a > b:
        summa = summa + a
        if b > c:
            summa = summa + b
        else:
            summa = summa + c
    else:
        summa = summa + b
        if a > c:
            summa = summa + a
        else:
            summa = summa + c
    return summa


print('Время выполнения функций')
print('my_func_sort :', timeit(
    "my_func_sort(3,4,6)", globals=globals(), number=10000))
print('my_func :', timeit("my_func(3,4,6)", globals=globals(), number=10000))
