class Cell:
    def __init__(self, cells):
        self.cells = cells

    def __add__(self, other):
        return Cell(self.cells + other.cells)

    def __sub__(self, other):
        return Cell(self.cells - other.cells) if self.cells - other.cells > 0 else print('Not allowed')

    def __mul__(self, other):
        return Cell(self.cells * other.cells)

    def __truediv__(self, other):
        return Cell(self.cells // other.cells)

    def __str__(self):
        return f'Общее количество ячеек --> {self.cells}'

    def make_order(self, arg):
        i = 0
        for cell in range(self.cells):
            if i == arg:
                i = 0
                print()
            print('1', end='')
            i += 1
        print()


cell1 = Cell(57)
cell2 = Cell(5)
cell3 = cell1 * cell2
print(cell3)
cell4 = cell1 / cell2
print(cell4)
cell5 = cell1 - cell2
print(cell5)
cell6 = cell1 + cell2
print(cell6)
cell3.make_order(79)
cell2 - cell1
