"""
3. Реализовать структуру «Рейтинг», представляющую собой не
возрастающий набор натуральных чисел
(каждый элемент ряда меньше или равен предыдущему).

У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.

Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.

Набор натуральных чисел можно задать непосредственно в коде,
например, my_list = [7, 5, 3, 3, 2].
"""
rating = [9, 7, 6, 6, 5, 5, 3]
rating_user = int(input("Введите цифру рейтинга : "))
if rating_user > rating[0]:
    rating.insert(0, rating_user)
if rating_user < rating[-1]:
    rating.append(rating_user)
i = 0
for i in range(len(rating)):
    if rating_user > rating[i]:
        rating.insert(i, rating_user)
        break
i += 1
print(rating)
