"""
2) Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

count_line = 0  # количество строк в тексте
count_words = 0  # количество слов в строке
count_symbols = 0  # количество символов в слове

with open('text1.txt', 'r', encoding='utf-8') as text:
    for line in text:
        print()
        count_line += 1
        count_words = len(line.split())
        print(f'количество слов в строке "{line}" = {count_words}')
        print()
        for el in line.split():
            count_symbols = len(el.strip('\n'))
            print(f'Количество символов в слове "{el}" = {count_symbols}')
    print()
    print(f'Количество строк в тексте {count_line}')
