class Car:
    def __init__(self, speed, colour, name, is_police=False):
        self.speed = speed
        self.colour = colour
        self.name = name
        self.is_police = is_police
        if is_police:
            self.name = 'мусор'

    def go(self):
        print(f'Движется вперед со скоростью - {self.speed}')

    def stop(self):
        print('Тормозит')

    def turn(self, direction):
        print(f'поворачивает {direction}')

    def show_speed(self):
        print(f'текущая скорость - {self.speed}км/ч')


class TownCar(Car):
    def go(self):
        if self.speed > 60:
            print('Нужно построить зиккурат!')
        else:
            print(f'Движется вперед со скоростью - {self.speed}')


class SportCar(Car):
    def go(self):
        if self.speed < 60:
            print('Дави на газ!')
        else:
            print('Со скоростью на скоростях и с Anime Power! Мчимся по белым дорогам!')


class WorkCar(Car):
    def go(self):
        if self.speed > 40:
            print('Нужно построить зиккурат!')
        else:
            print(f'Движется вперед со скоростью - {self.speed}')


class PoliceCar(Car):
    def who_is_he(self):
        print(self.name)


town_car = TownCar(61, 'red', 'Kia')
town_car.go()
sport_car = SportCar(120, 'black', 'Wololo')
sport_car.go()
work_car = WorkCar(47, 'purple', 'Hyundai')
work_car.go()
police_car = PoliceCar(60, 'any', 'guess_who', True)
police_car.who_is_he()
