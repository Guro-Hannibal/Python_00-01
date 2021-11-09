from abc import ABC, abstractmethod

# Я конечно впихну сюда абстрактный класс, но он здесь вообще не к месту. Property еще можно как-то притянуть за уши.


class Clothes(ABC):
    @abstractmethod
    def __init__(self, arg):
        pass

    @abstractmethod
    def consumption(self):
        pass

    # def __add__(self, other):
    #     return self.consumption + other.consumption


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def consumption(self):
        return self.size / 5 + 0.5


class Suit(Clothes):
    def __init__(self, height):
        self.height = height

    @property
    def consumption(self):
        return self.height * 2 + 0.3


coat = Coat(100)
suit = Suit(170)

print(f'Total consumption = {coat.consumption + suit.consumption}')

print(coat.consumption)

print(suit.consumption)

# print(coat + suit)
