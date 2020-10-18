class Stationery:
    def __init__(self, name):
        self.name = name


    def draw(self):
        print("Запуск отрисовки.")


stationery = Stationery("Канцелярская принадлежность")
stationery.draw()

class Pen(Stationery):
    def draw(self):
        print(f"Запуск отрисовки {stationery.name}.")

stationery = Pen("Ручка")
stationery.draw()

class Pencil(Stationery):
    def draw(self):
        print(f"Запуск отрисовки {stationery.name}.")


stationery = Pen("Карандаш")
stationery.draw()


class Handle(Stationery):
    def draw(self):
        print(f"Запуск отрисовки {stationery.name}.")


stationery = Pen("Маркер")
stationery.draw()
