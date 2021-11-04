import time


class TrafficLight:
    __color = None

    def running(self, count=2):
        TrafficLight.__color = 'red'
        print(TrafficLight.__color)
        time.sleep(7)
        TrafficLight.__color = 'yellow'
        print(TrafficLight.__color)
        time.sleep(3)
        TrafficLight.__color = 'green'
        print(TrafficLight.__color)
        time.sleep(7)
        count -= 1
        if count == 0:
            return
        self.running(count)


test = TrafficLight()

test.running(5)
