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

    # def first_try_add(self, other):
    #     i = 0
    #     if len(self.list_demo[0]) >= len(other.list_demo[0]):
    #         while i < len(other.list_demo[0]):
    #             y = 0
    #             for el in other.list_demo[i]:
    #                 self.list_demo[i][y] += el
    #                 y += 1
    #             i += 1
    #         print('If first matrix is bigger or equal to the second')
    #     else:
    #         while i < len(self.list_demo[0]):
    #             y = 0
    #             for el in self.list_demo[i]:
    #                 self.list_demo[i][y] += el
    #                 y += 1
    #             i += 1
    #         print('If second matrix is bigger')

    def __add__(self, other):
        i = 0
        while i < len(other.list_demo):
            y = 0
            for el in other.list_demo[i]:
                try:
                    self.list_demo[i][y] += el
                except IndexError:
                    self.list_demo[i].append(el)
                y += 1
            i += 1


list_matrix = [[1, 1, 1, 5], [2, 2, 2, 5], [3, 3, 3, 5]]

matrix = Matrix(list_matrix)

matrix_2 = Matrix([[1, 1, 1, 543, 645], [2, 2, 2, 564, -564], [3, 3, 3, 543, 5436]])

str(matrix)

# matrix + matrix_2
print('---------------------------------------------------')
# str(matrix)

matrix+matrix_2

str(matrix)
