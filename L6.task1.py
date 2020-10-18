import time
class TrafficLight:
    def __init__(self, color):
        self.__color = color

    def ring(self, colors):
        if colors == "RED":
            print(colors)
            time.sleep(7)
        elif colors == "YELLOW":
            print(colors)
            time.sleep(2)
        elif colors == "GREEN":
            print(colors)
            time.sleep(10)


traffic = TrafficLight('red')
traffic_color = ("RED", "YELLOW", "GREEN")
for i in range(0, len(traffic_color), 1):
    traffic.ring(traffic_color[i])
print("END")