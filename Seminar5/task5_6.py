"""
Задание 6. В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
Решите через рекурсию. В задании нельзя применять циклы.
"""


""" number_user - число, которое вводит пользователь
    number_random - загаданное число
    count_attempt - количество попыток = 10
"""

from random import randint
def random_number(number_user, number_random = randint(0, 100), count_attempt = 0):
    
    if number_user == number_random:
        print(f'Вы угадали число! {number_random}')
        return
    
    if count_attempt == 10:
        print(f'Количество попыток закончилось. Было загадано число {number_random}')
        return
    else:
        if number_user > number_random:
            print(f'Введенное число больше загаданного')
        else:
            print(f'Введенное число меньше загаданного')
    return(random_number(number_user = int(input('Введите загаданное число - ')), count_attempt = count_attempt + 1))
 
random_number(number_user = int(input('Введите загаданное число - '))) 
