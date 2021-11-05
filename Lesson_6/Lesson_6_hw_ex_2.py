class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def mass(self, mass_for_1sm, count_sm):
        print(f'{self._width}м * {self._length}м * {mass_for_1sm}кг * {count_sm}см '
              f'= {(self._width * self._length * mass_for_1sm * count_sm / 1000)}т')


road = Road(5000, 20)
road.mass(25, 5)
