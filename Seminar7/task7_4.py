"""
Задание 4.
Реализуйте базовый класс Car. У данного класса должны быть следующие публичные атрибуты:
speed, color, name, is_police (булево).
А также публичные методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс публичный метод show_speed,
который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""

from random import choice  # для случайного выбора налево/направо


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'Автомобиль {self.name} поехал'

    def stop(self):
        return f'Автомобиль {self.name} остановился'

    def turn(self, direction):
        direction = choice(direct)  # выбор случайного направления для поворота
        return f'Автомобиль {self.name} повернул {direction}'

    def show_speed(self):
        return f'Текущая скорость автомобиля {self.name} = {self.speed}  км/ч'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(
            f'Текущая скорость автомобиля {self.name} в городе = {self.speed} км/ч')

        if self.speed > 60:
            return f'Скорость {self.name} более 60 км/ч. СКОРОСТЬ ПРЕВЫШЕНА ! '


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(
            f'Текущая скорость служебного автомобиля {self.name} = {self.speed} км/ч')

        if self.speed > 40:
            return f'Скорость {self.name} более 40 км/ч. СКОРОСТЬ ПРЕВЫШЕНА ! '


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

# создаем экземпляры для классов


volvo = Car(120, ',бордовый', 'Volvo', False)
volkswagen = TownCar(100, 'черный', 'Volkswagen', False)
audi = SportCar(30, 'белый', 'Audi Sport', False)
reno = WorkCar(70, 'красный', 'Reno', True)
peugeot = PoliceCar(110, 'серый',  'Peugeot', True)
direct = ['налево', 'направо', 'назад']

# доступ к атрибутам и результат
print('РЕЗУЛЬТАТ ДОСТУПА К АТРИБУТАМ\n')
print(f'Скорость Volvo - {volvo.speed} км/ч')
print(f'Цвет Audi - {audi.color}')
print(f'Марка автомобиля - {reno.name}')
print(f'Принадлежность Reno к полиции - {reno.is_police}\n')

# вызов методов и результат
print('РЕЗУЛЬТАТ ВЫЗОВА МЕТОДОВ\n')
print(volvo.go())
print(volkswagen.stop())
print(audi.turn(direct))  # в методе случайно выбирается направление
print(volkswagen.show_speed())  # метод вызывается из класса TownCar
print(reno.show_speed())  # метод вызывается из класса WorkCar
print(peugeot.show_speed())  # метод вызывается из класса Car
