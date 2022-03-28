class Car:

    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f'The {self.name} едет'

    def stop(self):
        return f'\nThe {self.name} остановилась'

    def turn(self, direction):
        return f'\nThe {self.name} повернула {direction}'

    def show_speed(self):
        return f'\nВаша скорость - {self.speed} км/ч'


class TownCar(Car):
    def show_speed(self):
        # def __init__(self, speed, color, name, is_police):
        #     super().__init__(speed, color, name, is_police)
        if self.speed > 60:
            return f'\nВаша скорость выше разрешенной {self.speed} км/ч'
        else:
            return f'Скорость {self.name} не превышена'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\nВаша скорость выше разрешенной {self.speed} км/ч'
        else:
            return f'Скорость {self.name} не превышена'


class PoliceCar(Car):
    pass


town = TownCar('Lexus ES', 80, 'белый', False)
print('1:\n' + town.go(), town.show_speed(), town.turn('налево'), town.turn('направо'), town.stop())

sport = SportCar('Aston Martin Vanquish', 190, 'серебристый', False)
print('2:\n' + sport.go(), sport.show_speed(), sport.turn('направо'), sport.stop())

work = WorkCar('Рено Дастер', 60, 'коричневая', False)
print('3:\n' + work.go(), work.show_speed(), work.turn('налево'), work.stop())

police = PoliceCar('УАЗ Патриот', 90, 'белая с синей полосой', True)
print('4:\n' + work.go(), work.show_speed(), work.turn('right'), work.stop())