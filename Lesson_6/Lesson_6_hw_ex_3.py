class Worker:
    def __init__(self, name, surname, position, _wage=None):
        if _wage is None:
            _wage = {'wage': 0, 'bonus': 0}
        else:
            _wage = {'wage': _wage[0], 'bonus': _wage[1]}
        self.name = name
        self.surname = surname
        self.position = position
        self._wage = _wage


class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_wage(self):
        return self._wage

    def set_wage(self, _wage, _bonus):
        self._wage = {'wage': _wage, 'bonus': _bonus}
        return True


human = Position('Vasya', 'Vaskin', 'na rabote')

print(human.get_full_name())
print(human.get_wage())
print(human.set_wage(10, 5))
print(human.get_wage())
