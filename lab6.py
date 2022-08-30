print('\nЗадание 6:')
from time import sleep
class TrafficLight:

    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        counter = 0
        while counter <= 3:
            if counter == 0:
                print(self.__color[counter])
                sleep(7)
            elif counter == 1:
                print(self.__color[counter])
                sleep(2)
            elif counter == 2:
                print(self.__color[counter])
                sleep(5)
            counter += 1


tl = TrafficLight()
tl.running()


print('\nЗадание 2:')
class Road:

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def mass(self, mas_per_m2, depth):
        print((self._length * self._width * mas_per_m2 * depth) / 1000)


r = Road(5000, 20)
r.mass(25, 5)


print('\nЗадание 3:')
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):

    def get_full_name(self):
        return (f'{self.surname} {self.name}')
    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']

a = Position('Petr', 'Petrov', 'proger', 10000, 5000)
print(a.get_full_name(), a.get_total_income())


print('\nЗадание 4:')
class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.color} {self.name} поехала')

    def stop(self):
        print(f'{self.color} {self.name} остановилась')

    def turn(self, direction):
        print(f'{self.color} {self.name} повернула {direction}')

    def show_speed(self):
        print(f'{self.color} {self.name} едет со скоростью {self.speed}')


class TownCar(Car):

    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f'{self.color} {self.name} превысила скорость!')


class WorkCar(Car):

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f'{self.color} {self.name} превысила скорость!')


class PoliceCar(Car):
    pass


class SportCar(Car):
    pass


town_car = TownCar(55, 'Синяя', 'Audi')
town_car.go(), town_car.show_speed(), town_car.turn("Влево"), town_car.turn("Влево"), town_car.turn("Вправо"), town_car.stop()
print(town_car.is_police)

work_car = WorkCar(45, 'Black', 'BMW')
work_car.go(), work_car.show_speed(), work_car.stop()
print(work_car.is_police)

police_car = PoliceCar(100, 'Gray', 'Ford', True)
police_car.go(), police_car.show_speed(), police_car.turn("Вправо"), police_car.turn("Влево"), police_car.stop()
print(police_car.is_police)

sport_car = SportCar(120, 'Red', 'Ferrari')
sport_car.go(), sport_car.show_speed(), sport_car.turn("Вправо"), sport_car.turn("Влево"), sport_car.stop()
print(sport_car.is_police)


print('\nЗадание 5:')
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):

    def draw(self):
        print(f'Так рисует {self.title}')
class Pencil(Stationery):

    def draw(self):
        print(f'Так рисует {self.title}')
class Handle(Stationery):

    def draw(self):
        print(f'Так рисует {self.title}')

pen = Pen('Ручка')
pen.draw()

pencil = Pencil('Карандаш')
pencil.draw()

handle = Handle('Маркер')
handle.draw()



