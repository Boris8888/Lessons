class Road:
    def __init__(self):
        self._length = float(input("Введите длину дороги в метрах: "))
        self._width = float(input("Введите ширину в метрах: "))
        self._alto = float(input("Введите толщину покрытия в сантиметрах: "))

    def mas_road(self, length, width, alto):
        print(f"Масса асфальта {(length * width * alto * 25) / 1000} тонн.")

    @property
    def length(self):
        return self._length

    @property
    def width(self):
        return self._width

    @property
    def alto(self):
        return self._alto


road = Road()
road.mas_road(road.length, road.width, road.alto)