"""
4) Задание на закрепление знаний по модулю json. Есть файл orders
в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий
его заполнение данными.

Для этого:
Создать функцию write_order_to_json(), в которую передается
5 параметров — товар (item), количество (quantity), цена (price),
покупатель (buyer), дата (date). Функция должна предусматривать запись
данных в виде словаря в файл orders.json. При записи данных указать
величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json()
с передачей в нее значений каждого параметра.

ПРОШУ ВАС НЕ УДАЛЯТЬ ИСХОДНЫЙ JSON-ФАЙЛ
ПРИМЕР ТОГО, ЧТО ДОЛЖНО ПОЛУЧИТЬСЯ

{
"orders": [
{
"item": "принтер",
"quantity": "10",
"price": "6700",
"buyer": "Ivanov I.I.",
"date": "24.09.2017"
},
{
"item": "scaner",
"quantity": "20",
"price": "10000",
"buyer": "Petrov P.P.",
"date": "11.01.2018"
}
]
}

вам нужно подгрузить JSON-объект
и достучаться до списка, который и нужно пополнять
а потом сохранять все в файл
"""

import json
from datetime import datetime


with open('1.json', encoding='utf-8') as f:
    obj = json.load(f)  # из json файла в словарь
    key_obj = obj.keys()
    list_obj = obj.get("orders")  # из словаря в список
    dict_new_obj = {}  # словарь с добавленными новыми данными для обновления в json файле

# с проверкой на правильность ввода данных


def write_order_to_json(item, quantity, price, buyer, date, dict_obj={}, list_new_obj=[]):

    date = date.strftime("%d.%m.%Y")  # преобразуем дату к формату дд.мм.гггг
    dict_obj = {'item': item, 'quantity': quantity, 'price': price,
                'buyer': buyer, 'date': date}  # словарь по каждому товару
    # каждый новый словарь по товару добавляем в список
    list_new_obj.append(dict_obj)
    stop = input('Для завершения введите 0 - ')
    if stop == '0':
        print(f'Ввод окончен')
        return list_new_obj  # функция возвращает список из словарей новых товароы
    else:
        try:
            return (write_order_to_json(item=input(f'наименование товара - '), quantity=int(input(f'количество - ')),
                                        price=float(input(f'цена - ')), buyer=input(f'покупатель - '),
                                        date=datetime.strptime(input(f'дата (дд.мм.гггг): '), "%d.%m.%Y")))
        except ValueError:
            print('Ошибка ввода данных!')
            quit()


try:
    list_new_obj = write_order_to_json(item=input(f'наименование товара - '), quantity=int(input(f'количество - ')),
                                       price=float(input(f'цена - ')), buyer=input(f'покупатель - '),
                                       date=datetime.strptime(input(f'дата (дд.мм.гггг): '), "%d.%m.%Y"))
except ValueError:
    print('Ошибка ввода данных!')
    quit()

for el in list_new_obj:
    # к имеющемуся списку словарей добавляет по одному словарю из нового списка
    list_obj.append(el)

# в пустой словарь добавляем ключ и аргументы(полученный список словарей)
dict_new_obj = dict_new_obj.fromkeys(key_obj, list_obj)
# для обновления в json файле

with open('1.json', 'w', encoding='utf-8') as f:  # новый словарь для перезаписи в файл json
    # ensure_ascii=False - для отображения русскими буквами
    json.dump(dict_new_obj, f, indent=4, ensure_ascii=False)
