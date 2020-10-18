class Car:
    def __init__(self, speed):
        self.speed = speed
        self.color = 0
        self.name = 0
        self.is_police = False
        #self.TownCar()

    def go(self):
        pass

    def stop(self):
        pass

    def turn(self, direction):
        print("Автомобиль повернул на ", direction)

    def show_speed(self):
        print("Скорость", car_speed.speed, "km/h")

car_speed = Car(20)
car_speed.show_speed()
car_speed.turn("Право")

class TownCar(Car):
    def show_speed(self):
        if car_speed.speed > 60:
            print(f"Превышение скорости! Скорость - {car_speed.speed} km/h")
        else:
            print(f"Скорость городского автомобиля {car_speed.speed} km/h")

car_speed = TownCar(61)
car_speed.show_speed()
car_speed.turn("Лево")


class WorkCar(Car):
    def show_speed(self):
        if car_speed.speed > 40:
            print(f"Превышение скорости! Скорость - {car_speed.speed} km/h")
        else:
            print(f"Скорость городского автомобиля {car_speed.speed} km/h")


car_speed = WorkCar(20)
car_speed.show_speed()


class PoliceCar(Car):
    pass

class SportCar(Car):
    pass