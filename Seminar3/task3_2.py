"""
Задание 5. Пользователь вводит строку из нескольких слов,
разделённых пробелами. Вывести каждое слово с новой строки.
Строки необходимо пронумеровать. Если слово длинное,
выводить только первые 10 букв в слове.

Пример:
Введите слова через пробел: раз два три
1. раз
2. два
3. три

Введите слова через пробел: раз перерефрижерированность
1. раз
2. перерефриж 
"""
list_user = input("Введите строку из нескольких слов через пробел: ").split()
i = 0
for i, el in enumerate(list_user, 1):
    print(i, el[:10])

# в строке 17 запись в одну строку двух строк
# list_user = input("Введите строку из нескольких слов через пробел: ")
# list_user = list_user.split() - одной строкой