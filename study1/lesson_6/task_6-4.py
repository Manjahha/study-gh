class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} is started'

    def stop(self):
        return f'{self.name} is stopped'

    def turn_right(self):
        return f'{self.name} is turned right'

    def turn_left(self):
        return f'{self.name} is turned left'

    def show_speed(self):
        return f'Current speed {self.name} is {self.speed}'

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed {self.name} is {self.speed}')

        if self.speed > 40:
            return f'Speed of {self.name} is higher'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed {self.name} is {self.speed}')

        if self.speed > 60:
            return f'Speed of {self.name} is limit violated'

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} is police'

ferrari = SportCar(100, 'black', 'ferrari', False)
lada = TownCar(30, 'silver', 'Lada', False)
shevrole = WorkCar(50, 'grey', 'shevrole', False)
ford = PoliceCar(80, 'Blue',  'Ford', True)
print(lada.turn_left())
print(f'When {lada.turn_right()}, then {ferrari.stop()}')
print(f'{shevrole.go()} with speed exactly {shevrole.show_speed()}')
print(f'{shevrole.name} is {shevrole.color}')
print(f'Is {ferrari.name} a police car? {ferrari.is_police}')
print(f'Is {shevrole.name}  a police car? {shevrole.is_police}')
print(ferrari.show_speed())
print(lada.show_speed())
print(ford.police())
print(ford.show_speed())
