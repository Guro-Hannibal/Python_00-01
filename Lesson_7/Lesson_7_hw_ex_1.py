class Matrix:
    def __init__(self, list_demo):
        self.list_demo = list_demo

    def __str__(self):
        for el in self.list_demo:
            for num in el:
                print(str(num) + '    ', end='')
            print()
        return ''

    # def wololo(self):
    #     print([str(num) + '   ' for el in self.list_demo for num in el])

    def __add__(self, other):
        i = 0
        if len(self.list_demo[0]) >= len(other.list_demo[0]):
            while i < len(self.list_demo[0]):
                y = 0
                for el in other.list_demo[i]:
                    self.list_demo[i][y] += el
                    y += 1
                i += 1
            print('If first matrix is bigger or equal to the second')
        else:
            while i < len(other.list_demo[0]):
                y = 0
                for el in self.list_demo[i]:
                    other.list_demo[i][y] += el
                    y += 1
                i += 1
            print('If second matrix is bigger')


list_matrix = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]

matrix = Matrix(list_matrix)

matrix_2 = Matrix(list_matrix)

str(matrix)

matrix + matrix_2

str(matrix)