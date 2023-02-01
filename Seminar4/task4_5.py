"""
5. Сделайте профилирование кода любого или любых выполненных заданий
с помощью модуля timeit, опишите результат
"""

# С использованием функции sort() время выполнения быстрее

# используя функцию sort()
from timeit import timeit  # без sort()   0.13229730003513396
from timeit import timeit  # sort()   0.10654509998857975

print(timeit("""
def my_func(a, b, c = 0):
    list_1 = [a,b,c]
    list_1.sort()
    summa = b + c
    return summa
    """))

# без функции sort()

print(timeit("""
def my_func(a, b, c = 0):
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
    """))
