"""
Задание 1.
Создать класс TrafficLight (светофор)
и определить у него один приватный атрибут color (цвет) и публичный метод running (запуск).
В рамках метода running реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный)
составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение.
Для имитации "горения" каждого цвета испольщуйте ф-цию sleep модуля time
Переключение между режимами должно осуществляться только
в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""

from time import sleep

# создаем класс


class TrafficLight:
    # определяем приватный атрибут
    __colors = {'красный': 7, 'желтый': 2, 'зеленый': 10}

    def running(self):  # создаем ф-цию для переключения светофора
        for color, time_color in self.__colors.items():
            self.__colors = color
            print(
                f'На светофоре горит цвет - {self.__colors} в течение {time_color} секунд')

            # ф-ция приостанавливает выполнение программы на указанное время
            sleep(time_color)


t = TrafficLight()  # создаем экземпляр класса
t.running()  # запуск метода класса
