"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""

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


print(f"Сумма наибольших двух аргументов - {my_func(3,4,6)}")
