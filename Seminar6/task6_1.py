"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""

""" 
    вызовите командную строку Windows. После этого укажите имя интерпретатора python, 
    путь к вызываемому файлу и три значения, разделяя все пробелами
"""
"""
    name - фамилия сотрудника
    time - отработанное время
    hourly_rate - ставка в час
    bonus - процент премии
"""

from sys import argv
name_script, name, time, hourly_rate, bonus = argv

try:
    name = str(name)
    time = int(time)
    hourly_rate = int(hourly_rate)
    bonus = int(bonus)

    print(
        f'заработная плата сотрудника {name} = {time * hourly_rate + bonus / 100}')
except:
    print('Ошибка в данных')
