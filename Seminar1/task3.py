"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""

n = int(input("Введите целое положительное число n=: "))
print(f'n + nn + nnn =  {n+(n*10+n)+(n*100+n*10+n)}') # результат 369