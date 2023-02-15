"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

import subprocess
import chardet

ping_args = [['ping', 'yandex.ru'], ['ping', 'youtube.com']]

for ping_element in ping_args:
    ping_process = subprocess.Popen(ping_element, stdout=subprocess.PIPE)
    for line in ping_process.stdout:
        res = chardet.detect(line)
        line = line.decode(res['encoding'])
        print(line)
