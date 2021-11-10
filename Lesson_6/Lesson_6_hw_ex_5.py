class Stationery:
    def __init__(self, title='скучно'):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('что-то уникальное1')


class Pencil(Stationery):
    def draw(self):
        print('что-то уникальное2')


class Handle(Stationery):
    def draw(self):
        print('что-то уникальное3')


stationery = Stationery()
stationery.draw()
pen = Pen()
pen.draw()
pencil = Pencil()
pencil.draw()
handle = Handle()
handle.draw()
