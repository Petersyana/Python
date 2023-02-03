"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""

# без функции sort()


def my_func(a, b, c=0):
    sum = 0
    if a > b:
        sum = sum + a
        if b > c:
            sum = sum + b
        else:
            sum = sum + c
    else:
        sum = sum + b
        if a > c:
            sum = sum + a
        else:
            sum = sum + c
    return sum


print(f"Сумма наибольших двух аргументов - {my_func(3,4,6)}")
