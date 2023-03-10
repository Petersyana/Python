"""
Задание 1.

Спортсмен занимается ежедневными пробежками.
В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня,
на который результат спортсмена составит не менее b километров.
Программа должна принимать значения параметров a и b
и выводить одно натуральное число — номер дня.

Например: a = 2, b = 3.
Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22
Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.
"""
distance_a = float(input("Введите результат пробега первого дня (в км): "))
distance_b = float(input("Введите результат, который нужно достичь (в км): "))
count_day = 1 # счетчик дней
while distance_a < distance_b:
    distance_a = distance_a + distance_a * 0.1
    count_day += 1
print(f'Спортсмен достигнет желаемого результата на {count_day} день')
