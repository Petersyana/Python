"""
Задание 3. Создать список и заполнить его элементами различных типов данных.
Реализовать проверку типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

Пример:
для списка [5, "string", 0.15, True, None]
результат

<class 'int'>
<class 'str'>
<class 'float'>
<class 'bool'>
<class 'NoneType'>
"""
list_task = [5, "string", 0.15, True, None]
for el in list_task:
    print(type(el))

# КАК НЕ НУЖНО ДЕЛАТЬ
# i = 0
# for i in range(len(list_task)):
#     print(type(list_task[i]))
